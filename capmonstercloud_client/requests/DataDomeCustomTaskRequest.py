from typing import Dict, Union
from pydantic import Field, field_validator, model_validator
from .CustomTaskRequestBase import CustomTaskRequestBase

class DataDomeCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='DataDome')
    metadata : Dict[str, str]

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('datadomeCookie') is None:
            raise TypeError(f'Expect that datadomeCookie will be defined.')
        if value.get('datadomeVersion') is not None and not isinstance(value.get('datadomeVersion'), str):
            raise TypeError(f'Expected datadomeVersion to be str')
        if value.get('captchaUrl') and value.get('htmlPageBase64'):
            raise TypeError(f'Expected only one of [captchaUrl, htmlPageBase64]')
        elif value.get('captchaUrl'):
            return {i: value[i] for i in value if i != 'htmlPageBase64'}
        elif value.get('htmlPageBase64'):
            return {i: value[i] for i in value if i != 'captchaUrl'}
        else:
            raise TypeError(f'Expected one of [captchaUrl, htmlPageBase64]')

    @model_validator(mode='before')
    def validate_datadome_proxy(cls, values):
        proxy = values.get('proxy')
        if proxy is None:
            raise RuntimeError(f'You are required to use your own proxies.')
        return values

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['proxyType'] = self.proxy.proxyType
        task['proxyAddress'] = self.proxy.proxyAddress
        task['proxyPort'] = self.proxy.proxyPort
        task['proxyLogin'] = self.proxy.proxyLogin
        task['proxyPassword'] = self.proxy.proxyPassword
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.domains is not None:
            task['domains'] = self.domains
        return task