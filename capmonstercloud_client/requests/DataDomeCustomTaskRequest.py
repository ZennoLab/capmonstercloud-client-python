from typing import Dict, Union
from pydantic import Field, field_validator, model_validator
from .CustomTaskRequestBase import CustomTaskRequestBase

class DataDomeCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving DataDome custom challenges.

    Attributes:
        captchaClass: The constant string value identifying the captcha
            class as "DataDome".
        metadata: A dictionary carrying DataDome-specific challenge data:
            the required captchaUrl and datadomeCookie, plus the optional
            datadomeVersion.
        proxy: Proxy settings to route the request through. Required for
            this task type — DataDome will not solve without your own proxy.
    """
    captchaClass: str = Field(default='DataDome', description='The constant string value identifying the captcha class as "DataDome".')
    metadata : Dict[str, str] = Field(..., description='A dictionary carrying DataDome-specific challenge data: the required captchaUrl and datadomeCookie, plus the optional datadomeVersion.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('datadomeCookie') is None:
            raise TypeError(f'Expect that datadomeCookie will be defined.')
        if value.get('datadomeVersion') is not None and not isinstance(value.get('datadomeVersion'), str):
            raise TypeError(f'Expected datadomeVersion to be str')
        if value.get('captchaUrl') is None:
            raise TypeError(f'Expect that captchaUrl will be defined.')
        return value

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