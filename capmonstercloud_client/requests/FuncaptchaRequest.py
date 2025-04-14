from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class FuncaptchaRequest(BaseRequestWithProxy):
    type: str = Field(default='FunCaptchaTask')
    websiteUrl: str
    websitePublicKey: str
    funcaptchaApiJSSubdomain: Optional[str] = Field(default=None)
    data: Optional[str] = Field(default=None)
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websitePublicKey'] = self.websitePublicKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        
        if self.funcaptchaApiJSSubdomain is not None:
            task['funcaptchaApiJSSubdomain'] = self.funcaptchaApiJSSubdomain
        if self.data is not None:
            task['data'] = self.data
        return task