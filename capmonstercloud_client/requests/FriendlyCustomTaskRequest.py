from typing import Dict, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class FriendlyCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='friendly')
    websiteKey: str = Field()
    metadata: Dict[str, str]

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('apiGetLib') is None:
            raise TypeError(f'Expect that apiGetLib will be defined.')
        else:
            if not isinstance(value.get('apiGetLib'), str):
                raise TypeError(f'Expect that apiGetLib will be str.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['metadata'] = self.metadata
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
