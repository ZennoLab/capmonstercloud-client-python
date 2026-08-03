from typing import Dict, Optional, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class MTCaptchaRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving MTCaptcha challenges.

    Attributes:
        type: The constant string value identifying the task type as "MTCaptchaTask".
        websiteUrl: The URL of the webpage containing the MTCaptcha challenge.
        websiteKey: The site key associated with the MTCaptcha widget on the webpage.
        pageAction: An optional action name associated with the MTCaptcha
            challenge, used by some site implementations.
        isInvisible: When set to True, specifies that the challenge
            being solved is an invisible MTCaptcha.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
    """

    type: str = Field(default="MTCaptchaTask", description='The task type identifier, always "MTCaptchaTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the MTCaptcha challenge.')
    websiteKey: str = Field(..., description='The site key associated with the MTCaptcha widget on the webpage.')
    pageAction: Optional[str] = Field(default=None, description='An optional action name associated with the MTCaptcha challenge.')
    isInvisible: Optional[bool] = Field(default=None, description='Whether the MTCaptcha challenge is an invisible one.')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Pass only a current Windows OS UA.')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task["type"] = self.type
        task["websiteURL"] = self.websiteUrl
        task["websiteKey"] = self.websiteKey
        if self.pageAction is not None:
            task["pageAction"] = self.pageAction
        if self.isInvisible is not None:
            task["isInvisible"] = self.isInvisible
        if self.userAgent is not None:
            task["userAgent"] = self.userAgent
        if self.proxy:
            task["proxyType"] = self.proxy.proxyType
            task["proxyAddress"] = self.proxy.proxyAddress
            task["proxyPort"] = self.proxy.proxyPort
            task["proxyLogin"] = self.proxy.proxyLogin
            task["proxyPassword"] = self.proxy.proxyPassword

        return task
