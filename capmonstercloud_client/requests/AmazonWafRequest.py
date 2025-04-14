from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class AmazonWafRequest(BaseRequestWithProxy):
    type: str = 'AmazonTask'
    websiteUrl: str
    challengeScript: str
    captchaScript: str
    websiteKey: str
    context: str
    iv: str
    cookieSolution: Optional[bool] = Field(default=None)

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['challengeScript'] = self.challengeScript
        task['captchaScript'] = self.captchaScript
        task['websiteKey'] = self.websiteKey
        task['context'] = self.context
        task['iv'] = self.iv
        
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        
        if self.cookieSolution is not None:
            task['cookieSolution'] = self.cookieSolution
        return task