from typing import Dict, Union
from pydantic import Field, field_validator, model_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TspdCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving TSPD (PerimeterX/HUMAN
    Bot Defender) custom challenges.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom module,
            fixed to "tspd" for this task type.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA, matching the one used when the tspdCookie and
            htmlPageBase64 were obtained.
        metadata: A dictionary carrying the challenge data required to solve
            the TSPD task, including the "tspdCookie" string and the
            "htmlPageBase64" string.
    """

    captchaClass: str = Field(default='tspd', description='Class (subtype) identifier of the custom module, fixed to "tspd".')
    userAgent: str = Field(description='Browser User-Agent to emulate. Pass only a current Windows OS UA, matching the one used when the tspdCookie and htmlPageBase64 were obtained.')
    metadata: Dict[str, str] = Field(description='Challenge data required to solve the task, including "tspdCookie" and "htmlPageBase64".')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('tspdCookie') is None:
            raise TypeError(f'tspdCookie must be defined inside metadata.')
        else:
            if not isinstance(value.get('tspdCookie'), str):
                raise TypeError(f'tspdCookie must be str.')
        if value.get('htmlPageBase64') is None:
            raise TypeError(f'htmlPageBase64 must be defined inside metadata.')
        else:
            if not isinstance(value.get('htmlPageBase64'), str):
                raise TypeError(f'htmlPageBase64 must be str.')
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
