from typing import Dict, Union
from pydantic import Field

from .CustomTaskRequestBase import CustomTaskRequestBase

class BasiliskCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Basilisk custom captcha
    challenges.

    Attributes:
        captchaClass: The class (subtype) identifier of the custom module,
            fixed to "Basilisk" for this task type.
        websiteKey: The site key associated with the Basilisk captcha on
            the webpage.
    """

    captchaClass: str = Field(default='Basilisk', description='Class (subtype) identifier of the custom module, fixed to "Basilisk".')
    websiteKey: str = Field(..., description='Site key associated with the Basilisk captcha on the webpage.')
    
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
        return task