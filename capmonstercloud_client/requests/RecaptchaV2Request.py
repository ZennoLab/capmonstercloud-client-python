from typing import Dict, Union, Optional
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class RecaptchaV2Request(BaseRequestWithProxy):
    
    type: str = Field(default="NoCaptchaTask")
    websiteUrl: str
    websiteKey: str
    dataSValue: Optional[str] = Field(default=None)
    userAgent: Optional[str] = Field(default=None)
    cookies: Optional[str] = Field(default=None)

    def getTaskDict(self) -> Dict[str, Union[str, int]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword

        if self.dataSValue is not None:
           task['recaptchaDataSValue'] = self.dataSValue
        
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent

        if self.cookies is not None:
            task['cookies'] = self.cookies

        return task
    