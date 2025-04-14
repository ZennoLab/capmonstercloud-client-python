import asyncio
import aiohttp

from http.client import HTTPException
from typing import Dict, Union

from .captchaResult import CaptchaResult
from .requestController import RequestController
from .exceptions import GetBalanceError, GetTaskError, GetResultError, UnknownRequestInstanceError
from .clientOptions import ClientOptions
from .requests import *
from .GetResultTimeouts import *
from .utils import parseVersion


_instance_config = (
    ((RecaptchaV2Request,), getRecaptchaV2Timeouts),
    ((RecaptchaV2EnterpriseRequest,), getRecaptchaV2EnterpriseTimeouts),
    ((RecaptchaV3ProxylessRequest), getRecaptchaV3Timeouts),
    ((ImageToTextRequest), getImage2TextTimeouts),
    ((FuncaptchaRequest,), getFuncaptchaTimeouts),
    ((HcaptchaRequest,), getHcaptchaTimeouts),
    ((GeetestRequest,), getGeetestTimeouts),
    ((TurnstileRequest,), getTurnstileTimeouts),
    ((RecaptchaComplexImageTaskRequest, HcaptchaComplexImageTaskRequest, 
      FunCaptchaComplexImageTaskRequest), getImage2TextTimeouts),
    ((DataDomeCustomTaskRequest,), getDatadomeTimeouts),
    ((TenDiCustomTaskRequest,), getTenDiTimeouts),
    ((BasiliskCustomTaskRequest,), getBasiliskTimeouts),
    ((AmazonWafRequest,), getAmazonWafTimeouts),
    ((BinanceTaskRequest,), getBinanceTimeouts),
    ((ImpervaCustomTaskRequest,), getImpervaTimeouts),
    ((RecognitionComplexImageTaskRequest), getCITTimeouts)
)


class CapMonsterClient:
    def __init__(self, 
                 options: ClientOptions) -> None:
        self.options = options
        self._headers = {'User-Agent': 
                         f'Zennolab.CapMonsterCloud.Client.Python/{parseVersion()}'}
    
    @property
    def headers(self):
        return self._headers

    async def get_balance(self) -> Dict[str, Union[int, float, str]]:
        body = {
            'clientKey' : self.options.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.options.service_url + '/getBalance',
                                    json=body, 
                                    timeout=aiohttp.ClientTimeout(total=self.options.client_timeout)) as resp:
                if resp.status != 200:
                    raise HTTPException(f'Cannot create task. Status code: {resp.status}.')
                result = await resp.json(content_type=None)
                if result.get('errorId') != 0:
                    raise GetBalanceError(f'Cannot get balance on reason {str(result)}')
                return result


    async def solve_captcha(self, request: Union[
                                                 RecaptchaV2EnterpriseRequest, 
                                                 RecaptchaV2Request,
                                                 RecaptchaV3ProxylessRequest,
                                                 RecaptchaComplexImageTaskRequest,
                                                 ImageToTextRequest, 
                                                 FuncaptchaRequest,
                                                 FunCaptchaComplexImageTaskRequest,
                                                 HcaptchaRequest,
                                                 HcaptchaComplexImageTaskRequest,
                                                 GeetestRequest,
                                                 DataDomeCustomTaskRequest,
                                                 TenDiCustomTaskRequest,
                                                 BasiliskCustomTaskRequest,
                                                 AmazonWafRequest,
                                                 BinanceTaskRequest,
                                                 ImpervaCustomTaskRequest,
                                                 TurnstileRequest,
                                                 RecognitionComplexImageTaskRequest],
                            ) -> Dict[str, str]:
        '''
        Non-blocking method for captcha solving. 

        Args:
            request : This object must be an instance of "requests", otherwise an exception will be thrown
        '''
        for instance_source, get_timeouts in _instance_config:
            if isinstance(request, instance_source):
                return await self._solve(request, get_timeouts())
        rs_all = ''.join('\n'+ x for x in REQUESTS)
        raise UnknownRequestInstanceError(f'Unknown request instance "{type(request)}", ' \
                                            f'expected that request will belong next instances: {rs_all}')
        
    async def _solve(self, request: Union[
                                          RecaptchaV2EnterpriseRequest, 
                                          RecaptchaV2Request,
                                          RecaptchaV3ProxylessRequest,
                                          RecaptchaComplexImageTaskRequest,
                                          ImageToTextRequest, 
                                          FuncaptchaRequest,
                                          FunCaptchaComplexImageTaskRequest,
                                          HcaptchaRequest,
                                          HcaptchaComplexImageTaskRequest,
                                          GeetestRequest,
                                          DataDomeCustomTaskRequest,
                                          TenDiCustomTaskRequest,
                                          BasiliskCustomTaskRequest,
                                          AmazonWafRequest,
                                          BinanceTaskRequest,
                                          ImpervaCustomTaskRequest,
                                          TurnstileRequest,
                                          RecognitionComplexImageTaskRequest],
                           timeouts: GetResultTimeouts,
                           ) -> Dict[str, str]:

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
                                    json=body, 
                                    timeout=aiohttp.ClientTimeout(total=self.options.client_timeout),
                                    headers=self.headers) as resp:
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
                                    json=body, 
                                    timeout=aiohttp.ClientTimeout(total=self.options.client_timeout),
                                    headers=self.headers) as resp:
                if resp.status != 200:
                    raise HTTPException(f'Cannot create task. Status code: {resp.status}.')
                else:
                    return await resp.json(content_type=None)
        