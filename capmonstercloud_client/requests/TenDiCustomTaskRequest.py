from typing import Dict, Union
from pydantic import Field, validator

from .proxy_info import ProxyInfo
from .TenDiCustomTaskRequestBase import TenDiCustomTaskRequestBase

class TenDiCustomTaskRequest(TenDiCustomTaskRequestBase, ProxyInfo):
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['proxyType'] = self.proxyType
        task['proxyAddress'] = self.proxyAddress
        task['proxyPort'] = self.proxyPort
        task['proxyLogin'] = self.proxyLogin
        task['proxyPassword'] = self.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task