from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class RecaptchaV2EnterpriseRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving reCAPTCHA v2 Enterprise challenges.

    Attributes:
        type: The constant string value identifying the task type as
            "RecaptchaV2EnterpriseTask".
        websiteUrl: The URL of the webpage containing the reCAPTCHA
            Enterprise challenge.
        websiteKey: The site key associated with the reCAPTCHA Enterprise
            widget on the webpage.
        enterprisePayload: Additional parameters passed to the reCAPTCHA
            Enterprise widget, such as a custom "s" value used by some
            implementations.
        apiDomain: The domain to load the reCAPTCHA API from, used when the
            challenge is served from a domain other than the default Google
            domain.
        pageAction: The action name configured for the reCAPTCHA Enterprise
            challenge on the target website.
        recaptchaDataSValue: The one-time token from the widget's "data-s"
            parameter, if present on the page.
        userAgent: The User-Agent string of the browser that should be
            emulated while solving the challenge.
        cookies: Cookies to be sent along with the request when solving the
            challenge.
    """
    type: str = Field(default='RecaptchaV2EnterpriseTask', description='The constant string value identifying the task type as "RecaptchaV2EnterpriseTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the reCAPTCHA Enterprise challenge.')
    websiteKey: str = Field(..., description='The site key associated with the reCAPTCHA Enterprise widget on the webpage.')
    enterprisePayload: Optional[str] = Field(default=None, description='Additional parameters passed to the reCAPTCHA Enterprise widget, such as a custom "s" value used by some implementations.')
    apiDomain: Optional[str] = Field(default=None, description='The domain to load the reCAPTCHA API from, used when the challenge is served from a domain other than the default Google domain.')
    pageAction: Optional[str] = Field(default=None, description='The action name configured for the reCAPTCHA Enterprise challenge on the target website.')
    recaptchaDataSValue: Optional[str] = Field(default=None, description='The one-time token from the widget\'s "data-s" parameter, if present on the page.')
    userAgent: Optional[str] = Field(default=None, description='The User-Agent string of the browser that should be emulated while solving the challenge.')
    cookies: Optional[str] = Field(default=None, description='Cookies to be sent along with the request when solving the challenge.')

    def getTaskDict(self) -> Dict[str, Union[str, int]]:
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
        if self.enterprisePayload is not None:
            task['enterprisePayload'] = {'s': self.enterprisePayload}
        if self.apiDomain is not None:
            task['apiDomain'] = self.apiDomain
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        if self.recaptchaDataSValue is not None:
            task['recaptchaDataSValue'] = self.recaptchaDataSValue
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.cookies is not None:
            task['cookies'] = self.cookies
        return task