from typing import Dict, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TemuCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Temu's custom captcha
    challenge.

    Attributes:
        captchaClass: The constant string value identifying the custom
            module class as "Temu".
        metadata: A dictionary carrying the additional data required to
            solve the captcha; must contain a "cookie" string value and no
            other keys.
    """

    captchaClass: str = Field(default='Temu', description='Class (subtype) identifier of the custom module, constant "Temu".')
    metadata: Dict[str, str] = Field(..., description='Additional data required to solve the captcha; must contain a "cookie" string value and no other keys.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('cookie') is None:
            raise TypeError(f'Expect that cookie will be defined.')
        else:
            if not isinstance(value.get('cookie'), str):
                raise TypeError(f'Expect that cookie will be str.')
        if not set(value.keys()).issubset(set(["cookie"])):
            raise TypeError(f'Allowed keys for metadata are "cookie"')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
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