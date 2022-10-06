from pydantic import Field
from typing import Dict, Union

from .GeetestRequestBase import GeetestRequestBase
from .proxy_info import ProxyInfo

class GeetestRequest(GeetestRequestBase, ProxyInfo):
    type: str = Field(default='GeeTestTask')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['gt'] = self.gt
        task['challenge'] = self.challenge
        task['proxyType'] = self.proxy_type
        task['proxyAddress'] = self.proxy_address
        task['proxyPort'] = self.proxy_port
        task['proxyLogin'] = self.proxy_login
        task['proxyPassword'] = self.proxy_password
        if self.geetestApiServerSubdomain is not None:
            task['geetestApiServerSubdomain'] = self.geetestApiServerSubdomain
        if self.geetestGetLib is not None:
            task['geetestGetLib'] = self.geetestGetLib
        if self.user_agent is not None:
            task['userAgent'] = self.user_agent
        return task