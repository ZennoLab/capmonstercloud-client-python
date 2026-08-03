from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class HuntCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving custom HUNT challenges.

    Attributes:
        captchaClass: The constant string value identifying the underlying
            captcha class as "HUNT".
        metadata: A dictionary of parameters required by the HUNT solver.
            Always requires "apiGetLib" (the URL of the HUNT JS script on
            the page). HUNT has two solving modes: fingerprint generation
            (only "apiGetLib" needed) and captcha solving (also requires
            "data", which must hold the "meta.token" value extracted from
            the page).
    """
    captchaClass: str = Field(default='HUNT', description='The constant string value identifying the underlying captcha class as "HUNT".')
    metadata: Dict[str, str] = Field(..., description='Dictionary of HUNT parameters. Always requires "apiGetLib". Also requires "data" (the "meta.token" value from the page) when solving a captcha rather than just generating a fingerprint.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('apiGetLib') is None:
            raise TypeError(f'apiGetLib must be defined inside metadata.')
        else:
            if not isinstance(value.get('apiGetLib'), str):
                raise TypeError(f'apiGetLib must be str.')
        if value.get('data') is not None and not isinstance(value.get('data'), str):
            raise TypeError(f'data must be str.')
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
