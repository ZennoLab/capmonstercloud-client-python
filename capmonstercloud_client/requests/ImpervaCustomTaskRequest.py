from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class ImpervaCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Imperva/Incapsula custom challenges.

    Attributes:
        captchaClass: The constant string value identifying the captcha class
            as "Imperva".
        metadata: A dictionary of Imperva-specific parameters, including the
            required incapsulaScriptUrl and incapsulaCookies values, and the
            optional reese84UrlEndpoint value.
        proxy: Proxy settings to route the request through. Required for
            this task type — Imperva will not solve without your own proxy.
    """
    captchaClass: str = Field(default='Imperva', description='The constant string value identifying the captcha class as "Imperva".')
    metadata : Dict[str, str] = Field(..., description='A dictionary of Imperva-specific parameters, including the required incapsulaScriptUrl and incapsulaCookies values, and the optional reese84UrlEndpoint value.')
    
    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('incapsulaScriptUrl') is None:
            raise TypeError(f'Expect that incapsulaScriptUrl will be defined.')
        else:
            if not isinstance(value.get('incapsulaScriptUrl'), str):
                raise TypeError(f'Expect that incapsulaScriptUrl will be str.')
        if value.get('incapsulaCookies') is None:
            raise TypeError(f'Expect that incapsulaCookies will be defined.')
        else:
            if not isinstance(value.get('incapsulaCookies'), str):
                raise TypeError(f'Expect that incapsulaCookies will be str.')
        if value.get('reese84UrlEndpoint') is not None and not isinstance(value.get('reese84UrlEndpoint'), str):
            raise TypeError(f'Expect that reese84UrlEndpoint will be str.')
        return value
    
    @model_validator(mode='before')
    def validate_imperva_proxy(cls, values):
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