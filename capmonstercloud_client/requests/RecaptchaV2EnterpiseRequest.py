from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class RecaptchaV2EnterpriseRequest(BaseRequestWithProxy):
    type: str = Field(default='RecaptchaV2EnterpriseTask')
    websiteUrl: str
    websiteKey: str
    enterprisePayload: Optional[str] = Field(default=None)
    apiDomain: Optional[str] = Field(default=None)
    
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
        if self.enterprisePayload is not None:
            task['enterprisePayload'] = {'s': self.enterprisePayload}
        if self.apiDomain is not None:
            task['apiDomain'] = self.apiDomain
        return task