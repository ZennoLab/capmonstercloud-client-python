from typing import Dict, Union
from pydantic import Field
from .TurnstileRequestBase import TurnstileRequestBase
from .proxy_info import ProxyInfo


class TurnstileRequest(TurnstileRequestBase, ProxyInfo):
    
    type: str = Field(default="TurnstileTask")

    def getTaskDict(self) -> Dict[str, Union[str, int]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['proxyType'] = self.proxy_type
        task['proxyAddress'] = self.proxy_address
        task['proxyPort'] = self.proxy_port
        task['proxyLogin'] = self.proxy_login
        task['proxyPassword'] = self.proxy_password
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
    