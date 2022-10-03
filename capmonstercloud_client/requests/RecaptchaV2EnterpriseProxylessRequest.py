from typing import Dict, Union
from pydantic import Field

from .RecaptchaV2EnterpriseRequestBase import RecaptchaV2EnterpriseRequestBase

class RecaptchaV2EnterpriseProxylessRequest(RecaptchaV2EnterpriseRequestBase):
    type: str = Field(default='RecaptchaV2EnterpriseTaskProxyless')

    def getTaskDict(self) -> Dict[str, Union[str, Dict[str, str]]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.enterprisePayload is not None:
            task['enterprisePayload'] = {'s': self.enterprisePayload}
        if self.apiDomain is not None:
            task['apiDomain'] = self.apiDomain
        return task