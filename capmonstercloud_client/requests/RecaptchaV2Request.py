from typing import Dict, Union, Optional
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class RecaptchaV2Request(BaseRequestWithProxy):
    """
    Represents a request payload for solving reCAPTCHA v2 challenges.

    Attributes:
        type: The constant string value identifying the task type as "RecaptchaV2Task".
        websiteUrl: The URL of the webpage containing the reCAPTCHA challenge.
        websiteKey: The site key associated with the reCAPTCHA on the webpage.
        dataSValue: A one-time token specific to certain custom
            implementations of reCAPTCHA v2. If applicable, this parameter needs
            to be retrieved for each challenge-solving attempt.
        userAgent: The User-Agent header of the browser to be emulated
            while solving the captcha. Must be a current/modern browser
            signature — a stale or non-standard UA causes Google to return
            an "update your browser" error instead of solving the captcha.
        cookies: Cookies to be used when accessing the target webpage
            while solving the captcha, formatted as "name1=value1; name2=value2".
        isInvisible: When set to True, specifies that the challenge
            being solved is an invisible reCAPTCHA.
    """

    type: str = Field(default="RecaptchaV2Task", description='The constant string value identifying the task type as "RecaptchaV2Task".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the reCAPTCHA challenge.')
    websiteKey: str = Field(..., description='The site key associated with the reCAPTCHA on the webpage.')
    dataSValue: Optional[str] = Field(default=None, description='A one-time token specific to certain custom implementations of reCAPTCHA v2, retrieved per challenge-solving attempt.')
    userAgent: Optional[str] = Field(default=None, description='The User-Agent header of the browser to be emulated while solving the captcha. Must be a current/modern browser signature, otherwise Google will return an error asking for a browser update.')
    cookies: Optional[str] = Field(default=None, description='Cookies to be used when accessing the target webpage while solving the captcha, formatted as "name1=value1; name2=value2".')
    isInvisible: Optional[bool] = Field(default=None, description='When set to True, specifies that the challenge being solved is an invisible reCAPTCHA.')

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

        if self.dataSValue is not None:
           task['recaptchaDataSValue'] = self.dataSValue

        if self.userAgent is not None:
            task['userAgent'] = self.userAgent

        if self.cookies is not None:
            task['cookies'] = self.cookies

        if self.isInvisible is not None:
            task['isInvisible'] = self.isInvisible

        return task
    