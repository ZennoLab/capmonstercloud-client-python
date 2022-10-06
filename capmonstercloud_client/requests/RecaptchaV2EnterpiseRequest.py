from typing import Dict, Union
from pydantic import Field

from .RecaptchaV2EnterpriseRequestBase import RecaptchaV2EnterpriseRequestBase
from .proxy_info import ProxyInfo

class RecaptchaV2EnterpriseRequest(RecaptchaV2EnterpriseRequestBase, ProxyInfo):
    type: str = Field(default='RecaptchaV2EnterpriseTask')

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
        if self.enterprisePayload is not None:
            task['enterprisePayload'] = {'s': self.enterprisePayload}
        if self.apiDomain is not None:
            task['apiDomain'] = self.apiDomain
        return task