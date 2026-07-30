from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TspdCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='tspd')
    userAgent: str = Field()
    metadata: Dict[str, str]

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('tspdCookie') is None:
            raise TypeError(f'Expect that tspdCookie will be defined.')
        else:
            if not isinstance(value.get('tspdCookie'), str):
                raise TypeError(f'Expect that tspdCookie will be str.')
        if value.get('htmlPageBase64') is None:
            raise TypeError(f'Expect that htmlPageBase64 will be defined.')
        else:
            if not isinstance(value.get('htmlPageBase64'), str):
                raise TypeError(f'Expect that htmlPageBase64 will be str.')
        return value

    @model_validator(mode='before')
    def validate_tspd_proxy(cls, values):
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
        task['userAgent'] = self.userAgent
        task['proxyType'] = self.proxy.proxyType
        task['proxyAddress'] = self.proxy.proxyAddress
        task['proxyPort'] = self.proxy.proxyPort
        task['proxyLogin'] = self.proxy.proxyLogin
        task['proxyPassword'] = self.proxy.proxyPassword
        return task
