from typing import Dict, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class FriendlyCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Friendly Captcha challenges.

    Attributes:
        captchaClass: The constant string value "friendly" identifying
            this custom task as a Friendly Captcha challenge.
        websiteKey: The site key associated with the Friendly Captcha
            widget on the webpage.
        metadata: Must contain the "apiGetLib" entry — the URL of the Friendly
            Captcha widget script loaded on the page (widget.module.min.js for
            V1, site.min.js for V2), used to detect the captcha version.
    """

    captchaClass: str = Field(default='friendly', description='Constant string "friendly" identifying this custom task as a Friendly Captcha challenge.')
    websiteKey: str = Field(..., description='Site key associated with the Friendly Captcha widget on the webpage.')
    metadata: Dict[str, str] = Field(..., description='Additional task parameters, must include the "apiGetLib" string entry.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('apiGetLib') is None:
            raise TypeError(f'Expect that apiGetLib will be defined.')
        else:
            if not isinstance(value.get('apiGetLib'), str):
                raise TypeError(f'Expect that apiGetLib will be str.')
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
