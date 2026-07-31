from typing import Dict, Optional, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TenDiCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving TenDI custom captcha challenges.

    Attributes:
        captchaClass: The identifier of the custom captcha class to solve,
            defaulting to "TenDI".
        websiteKey: The captchaAppId (the "aid" value, e.g. "189123456") for
            the target website, found in the page HTML or network traffic.
        metadata: Optional additional parameters for the task. Currently
            supports the "captchaUrl" key, whose value must be a string.
    """
    captchaClass: str = Field(default='TenDI', description='The identifier of the custom captcha class to solve.')
    websiteKey: str = Field(description='The captchaAppId (the "aid" value, e.g. "189123456") for the target website, found in the page HTML or network traffic.')
    metadata: Optional[Dict[str, str]] = Field(default=None, description='Optional additional parameters for the task; supports the "captchaUrl" key with a string value.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value is not None:
            if not set(value.keys()).issubset(set(["captchaUrl"])):
                raise TypeError(f'Allowed keys for metadata are "captchaUrl"')
            if value.get('captchaUrl') is not None and not isinstance(value.get('captchaUrl'), str):
                raise TypeError(f'Expect that captchaUrl will be str.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.metadata is not None:
            task['metadata'] = self.metadata
        return task