from pydantic import Field
from typing import Dict, Union, Optional

from .baseRequestWithProxy import BaseRequestWithProxy

class HcaptchaRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving hCaptcha challenges.

    Attributes:
        type: The constant string value identifying the task type as "HCaptchaTask".
        websiteUrl: The URL of the webpage containing the hCaptcha challenge.
        websiteKey: The site key associated with the hCaptcha on the webpage.
        is_invisible: When set to True, specifies that the challenge
            being solved is an invisible hCaptcha.
        data: The value of the optional "data" attribute used by some
            hCaptcha implementations, if present on the target page.
        user_agent: The User-Agent string of the browser to associate
            with the solving session.
        cookies: Cookies to be used during the solving process, formatted
            as a single string of "name1=value1; name2=value2" pairs.
        fallbackToActualUA: When set to True, allows the worker's actual
            User-Agent to be used as a fallback if a specific one is not required.
    """
    type: str = Field(default='HCaptchaTask', description='The constant string value identifying the task type as "HCaptchaTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the hCaptcha challenge.')
    websiteKey: str = Field(..., description='The site key associated with the hCaptcha on the webpage.')
    is_invisible: Optional[bool] = Field(default=None, description='When set to True, specifies that the challenge being solved is an invisible hCaptcha.')
    data: Optional[str] = Field(default=None, description='The value of the optional "data" attribute used by some hCaptcha implementations, if present on the target page.')
    user_agent: Optional[str] = Field(default=None, description='The User-Agent string of the browser to associate with the solving session.')
    cookies: Optional[str] = Field(default=None, description='Cookies to be used during the solving process, formatted as a single string of "name1=value1; name2=value2" pairs.')
    fallbackToActualUA: Optional[bool] = Field(default=None, description="When set to True, allows the worker's actual User-Agent to be used as a fallback if a specific one is not required.")

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:

        task = {}       
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.is_invisible is not None:
            task['isInvisible'] = self.is_invisible
        if self.data is not None:
            task['data'] = self.data
        if self.user_agent is not None:
            task['userAgent'] = self.user_agent
        if self.cookies is not None:
            task['cookies'] = self.cookies
        if self.fallbackToActualUA is not None:
            task['fallbackToActualUA'] = self.fallbackToActualUA

        return task