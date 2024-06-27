from typing import Dict, Union
from pydantic import Field, validator

from .proxy_info import ProxyInfo
from .AmazonWafRequestBase import AmazonWafRequestBase

class AmazonWafRequest(AmazonWafRequestBase, ProxyInfo):
    type: str = 'AmazonTask'

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['challengeScript'] = self.challengeScript
        task['captchaScript'] = self.captchaScript
        task['websiteKey'] = self.websiteKey
        task['context'] = self.context
        task['iv'] = self.iv

        task['proxyType'] = self.proxyType
        task['proxyAddress'] = self.proxyAddress
        task['proxyPort'] = self.proxyPort
        task['proxyLogin'] = self.proxyLogin
        task['proxyPassword'] = self.proxyPassword
        
        if self.cookieSolution is not None:
            task['cookieSolution'] = self.cookieSolution
        return task