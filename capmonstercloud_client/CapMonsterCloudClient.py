import asyncio
import aiohttp

from http.client import HTTPException
from typing import Dict, Union, Type

from .captchaResult import CaptchaResult
from .requestController import RequestController
from .exceptions import GetBalanceError, GetTaskError, GetResultError, UnknownRequestInstanceError
from .clientOptions import ClientOptions
from .requests import *
from .GetResultTimeouts import *


class CapMonsterClient:
    def __init__(self, options: ClientOptions) -> None:
        self.options = options
        self.client_timeout = aiohttp.ClientTimeout(total=20.0)

    async def get_balance(self) -> Dict[str, Union[int, float, str]]:
        body = {
            'clientKey' : self.options.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.options.service_url + '/getBalance',
                                    json=body, timeout=self.client_timeout) as resp:
                if resp.status != 200:
                    raise HTTPException(f'Cannot create task. Status code: {resp.status}.')
                result = await resp.json(content_type=None)
                if result.get('errorId') != 0:
                    raise GetBalanceError(f'Cannot get balance on reason {str(result)}')
                return result


    async def solve_captcha(self, request: Union[RecaptchaV2EnterpriseProxylessRequest,
                                                 RecaptchaV2EnterpriseRequest, RecaptchaV2Request, 
                                                 RecaptchaV2ProxylessRequest, RecaptchaV3ProxylessRequest,
                                                 ImageToTextRequest, FuncaptchaProxylessRequest,
                                                 FuncaptchaRequest, HcaptchaRequest, HcaptchaProxylessRequest,
                                                 GeetestProxylessRequest, GeetestRequest]) -> Dict[str, str]:
        '''
        Non-blocking method for captcha solving. 

        Args:
            request : This object must be an instance of "requests", otherwise an exception will be thrown
        '''
        if isinstance(request, RecaptchaV2ProxylessRequest):
            return await self._solve(request, getRecaptchaV2Timeouts())
        elif isinstance(request, RecaptchaV2Request):
            return await self._solve(request, getRecaptchaV2Timeouts())
        elif isinstance(request, RecaptchaV2EnterpriseProxylessRequest):
            return await self._solve(request, getRecaptchaV2EnterpriseTimeouts())
        elif isinstance(request, RecaptchaV2EnterpriseRequest):
            return await self._solve(request, getRecaptchaV2EnterpriseTimeouts())
        elif isinstance(request, ImageToTextRequest):
            return await self._solve(request, getImage2TextTimeouts())
        elif isinstance(request, RecaptchaV3ProxylessRequest):
            return await self._solve(request, getRecaptchaV3Timeouts())
        elif isinstance(request, HcaptchaProxylessRequest):
            return await self._solve(request, getHcaptchaTimeouts())
        elif isinstance(request, HcaptchaRequest):
            return await self._solve(request, getHcaptchaTimeouts())
        elif isinstance(request, FuncaptchaProxylessRequest):
            return await self._solve(request, getFuncaptchaTimeouts())
        elif isinstance(request, FuncaptchaRequest):
            return await self._solve(request, getFuncaptchaTimeouts())
        elif isinstance(request, GeetestProxylessRequest):
            return await self._solve(request, getGeetestTimeouts())
        elif isinstance(request, GeetestRequest):
            return await self._solve(request, getGeetestTimeouts())
        else:
            rs_all = ''.join('\n'+ x for x in REQUESTS)
            raise UnknownRequestInstanceError(f'Unknown request instance "{type(request)}", ' \
                                              f'expected that request will belong next instances: {rs_all}')
        
    async def _solve(self, request: BaseRequest, timeouts: Type[GetResultTimeouts]) -> Dict[str, str]:

        getTaskResponse = await self._createTask(request)
        if getTaskResponse.get('errorId') != 0:
            raise GetTaskError(f'[{getTaskResponse.get("errorCode")}] ' \
                               f'{getTaskResponse.get("errorDescription")}.')
        timer = RequestController(timeout=timeouts.timeout)
        await asyncio.sleep(timeouts.firstRequestDelay)
        result = CaptchaResult()
        while not timer.cancel:
            getResultResponse = await self._getTaskResult(getTaskResponse.get('taskId'))

            if getResultResponse.get('errorId') != 0:
                timer.stop()
                raise GetResultError(f'[{getResultResponse.get("errorCode")}] ' \
                                     f'{getResultResponse.get("errorDescription")}.')

            if getResultResponse.get('status') == 'processing':
                await asyncio.sleep(timeouts.requestsInterval)
                continue

            elif getResultResponse.get('status') == 'ready':
                timer.stop()
                result.solution = getResultResponse.get('solution')
                break
        
        if result != None:
            return result.solution
        else:
            raise TimeoutError('Failed to get a solution within the maximum ' \
                               f'response waiting interval: {timeouts.timeout:0.1f} sec.')
        

    async def _getTaskResult(self, task_id: str) -> Dict[str, Union[int, str, None]]:
        body = {
            'clientKey': self.options.api_key,
            'taskId': task_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.options.service_url + '/getTaskResult',
                                    json=body, timeout=self.client_timeout) as resp:
                if resp.status != 200:
                    if resp.status == 500:
                        return {'errorId': 0, 'status': 'processing'}
                    else:
                        raise HTTPException(f'Cannot grab result. Status code: {resp.status}.')
                else:
                    return await resp.json(content_type=None)

    async def _createTask(self, request: BaseRequest) -> Dict[str, Union[str, int]]:
        task = request.getTaskDict()
        body = {
                "clientKey": self.options.api_key,
                "task": task,
                "softId": self.options.default_soft_id
               }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.options.service_url + '/createTask',
                                    json=body, timeout=self.client_timeout) as resp:
                if resp.status != 200:
                    raise HTTPException(f'Cannot create task. Status code: {resp.status}.')
                else:
                    return await resp.json(content_type=None)
        