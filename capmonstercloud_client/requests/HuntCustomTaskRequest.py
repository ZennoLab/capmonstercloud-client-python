from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class HuntCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='HUNT')
    metadata: Dict[str, str]

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('apiGetLib') is None:
            raise TypeError(f'Expect that apiGetLib will be defined.')
        else:
            if not isinstance(value.get('apiGetLib'), str):
                raise TypeError(f'Expect that apiGetLib will be str.')
        if value.get('data') is not None and not isinstance(value.get('data'), str):
            raise TypeError(f'Expect that data will be str.')
        return value

    @model_validator(mode='before')
    def validate_hunt_proxy(cls, values):
        proxy = values.get('proxy')
        if proxy is None:
            raise RuntimeError(f'You are required to use your own proxies.')
        return values

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['metadata'] = self.metadata
        task['proxyType'] = self.proxy.proxyType
        task['proxyAddress'] = self.proxy.proxyAddress
        task['proxyPort'] = self.proxy.proxyPort
        task['proxyLogin'] = self.proxy.proxyLogin
        task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
