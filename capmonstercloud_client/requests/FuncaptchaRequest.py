from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class FuncaptchaRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving FunCaptcha (Arkose Labs) challenges.

    Attributes:
        type: The constant string value identifying the task type as "FunCaptchaTask".
        websiteUrl: The URL of the webpage containing the FunCaptcha challenge.
        websitePublicKey: The public key (site key) associated with the
            FunCaptcha challenge on the webpage.
        funcaptchaApiJSSubdomain: A custom subdomain used by some FunCaptcha
            implementations to load the API JS script. Required only if the
            target website uses a non-default subdomain.
        data: Additional custom data required by certain FunCaptcha
            implementations, typically passed as a JSON string with extra
            parameters such as "blob".
        cookies: Cookies to be used when accessing the target webpage,
            provided as a string of key-value pairs.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
    """
    type: str = Field(default='FunCaptchaTask', description='The task type identifier, "FunCaptchaTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the FunCaptcha challenge.')
    websitePublicKey: str = Field(..., description='The public key (site key) associated with the FunCaptcha challenge on the webpage.')
    funcaptchaApiJSSubdomain: Optional[str] = Field(default=None, description='A custom subdomain used by some FunCaptcha implementations to load the API JS script.')
    data: Optional[str] = Field(default=None, description='Additional custom data required by certain FunCaptcha implementations (e.g. a JSON string containing "blob").')
    cookies: Optional[str] = Field(default=None, description='Cookies to be used when accessing the target webpage, provided as a string of key-value pairs.')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Pass only a current Windows OS UA.')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websitePublicKey'] = self.websitePublicKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        
        if self.funcaptchaApiJSSubdomain is not None:
            task['funcaptchaApiJSSubdomain'] = self.funcaptchaApiJSSubdomain
        if self.data is not None:
            task['data'] = self.data
        if self.cookies is not None:
            task['cookies'] = self.cookies
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task