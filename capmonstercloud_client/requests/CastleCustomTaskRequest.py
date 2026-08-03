from typing import Dict, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class CastleCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Castle challenges via a custom task.

    Attributes:
        captchaClass: The constant string value identifying the captcha
            class as "Castle".
        websiteKey: The site key associated with the Castle challenge on the
            webpage.
        metadata: A dictionary of additional parameters required to solve the
            challenge, including the worker script URL (wUrl), service worker
            URL (swUrl), and an optional request count (count).
    """
    captchaClass: str = Field(default='Castle', description='The constant string value identifying the captcha class as "Castle".')
    websiteKey: str = Field(description='The site key associated with the Castle challenge on the webpage.')
    metadata: Dict[str, Union[str, int]] = Field(description='A dictionary of additional parameters required to solve the challenge, including the worker script URL (wUrl), service worker URL (swUrl), and an optional request count (count).')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('wUrl') is None:
            raise TypeError(f'Expected that wUrl is defined.')
        else:
            if not isinstance(value.get('wUrl'), str):
                raise TypeError(f'Expected that wUrl is str.')
        if value.get('swUrl') is None:
            raise TypeError(f'Expected that swUrl is defined.')
        else:
            if not isinstance(value.get('swUrl'), str):
                raise TypeError(f'Expected that swUrl is str.')
        if value.get('count') is not None and not isinstance(value.get('count'), int):
            raise TypeError(f'Expected that count is int.')
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
