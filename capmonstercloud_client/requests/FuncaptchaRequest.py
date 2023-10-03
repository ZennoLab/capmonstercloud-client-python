from typing import Dict, Union
from pydantic import Field

from .FuncaptchaRequestBase import FuncaptchaRequestBase
from .proxy_info import ProxyInfo

class FuncaptchaRequest(FuncaptchaRequestBase, ProxyInfo):
    type: str = Field(default='FunCaptchaTask')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websitePublicKey'] = self.websitePublicKey
        task['proxyType'] = self.proxyType
        task['proxyAddress'] = self.proxyAddress
        task['proxyPort'] = self.proxyPort
        task['proxyLogin'] = self.proxyLogin
        task['proxyPassword'] = self.proxyPassword
        if self.funcaptchaApiJSSubdomain is not None:
            task['funcaptchaApiJSSubdomain'] = self.funcaptchaApiJSSubdomain
        if self.data is not None:
            task['data'] = self.data
        return task