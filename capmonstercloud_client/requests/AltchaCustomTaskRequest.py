from typing import Dict, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class AltchaCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Altcha proof-of-work
    captcha challenges via a custom module.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom
            module, constant "altcha" for this task.
        websiteKey: The site key associated with the Altcha challenge
            on the webpage. An empty string is allowed for this task.
        metadata: A dictionary containing the Altcha challenge parameters
            (challenge, iterations, salt, signature) extracted from the
            webpage.
    """

    captchaClass: str = Field(default='altcha', description='Class (subtype) identifier of the custom module, constant "altcha".')
    websiteKey: str = Field(description='Site key associated with the Altcha challenge on the webpage. An empty string is allowed for this task.')
    metadata: Dict[str, str] = Field(description='Altcha challenge parameters: challenge, iterations, salt, and signature.')
    
    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        for key in ['challenge', 'iterations', 'salt', 'signature']:
            if value.get(key) is None:
                raise TypeError(f'{key} must be defined inside metadata.')
            else:
                if not isinstance(value.get(key), str):
                    raise TypeError(f'{key} must be str.')
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
