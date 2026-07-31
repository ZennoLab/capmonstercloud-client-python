from typing import Dict, Union, Optional
from pydantic import Field, model_validator

from .baseRequestWithProxy import BaseRequestWithProxy

class AmazonWafRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving Amazon AWS WAF captcha challenges.

    The live API accepts three mutually exclusive parameter sets:
        Option 1 (visible captcha): websiteUrl, websiteKey, captchaScript
            required; challengeScript/context/iv must not be set.
        Option 2 (challenge + captcha): websiteUrl, challengeScript, websiteKey,
            context, iv required; captchaScript optional.
        Option 3 (invisible/challenge-only): websiteUrl, challengeScript
            required; context and iv must be empty strings; websiteKey and
            captchaScript must not be set.

    Attributes:
        type: The constant string value identifying the task type as "AmazonTask".
        websiteUrl: The URL of the webpage where the Amazon AWS WAF challenge
            is presented.
        challengeScript: Link to challenge.js served by AWS WAF on the target
            page. Required for Options 2 and 3; must not be set for Option 1.
        captchaScript: Link to captcha.js / jsapi.js served by AWS WAF on the
            target page. Required for Option 1, optional for Option 2, must
            not be set for Option 3.
        websiteKey: The site key associated with the AWS WAF challenge.
            Required for Options 1 and 2; must not be set for Option 3.
        context: The context token provided by AWS WAF, used to correlate
            the challenge with a specific session. Required for Option 2;
            must be an empty string for Option 3; must not be set for Option 1.
        iv: The initialization vector value provided by AWS WAF as part
            of the challenge payload. Required for Option 2; must be an
            empty string for Option 3; must not be set for Option 1.
        cookieSolution: When set to True, requests the solution to be
            returned as a ready-to-use cookie instead of a token.
        userAgent: Browser User-Agent to emulate. Only used for Option 1.
            Pass only a current Windows OS UA.
    """
    type: str = Field(default='AmazonTask', description='The constant string value identifying the task type as "AmazonTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage where the Amazon AWS WAF challenge is presented.')
    challengeScript: Optional[str] = Field(default=None, description='Link to challenge.js served by AWS WAF on the target page. Required for Options 2 and 3; must not be set for Option 1.')
    captchaScript: Optional[str] = Field(default=None, description='Link to captcha.js / jsapi.js served by AWS WAF on the target page. Required for Option 1, optional for Option 2, must not be set for Option 3.')
    websiteKey: Optional[str] = Field(default=None, description='The site key associated with the AWS WAF challenge. Required for Options 1 and 2; must not be set for Option 3.')
    context: Optional[str] = Field(default=None, description='The context token provided by AWS WAF, used to correlate the challenge with a specific session. Required for Option 2; must be an empty string for Option 3; must not be set for Option 1.')
    iv: Optional[str] = Field(default=None, description='The initialization vector value provided by AWS WAF as part of the challenge payload. Required for Option 2; must be an empty string for Option 3; must not be set for Option 1.')
    cookieSolution: Optional[bool] = Field(default=None, description='When set to True, requests the solution to be returned as a ready-to-use cookie instead of a token.')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Only used for Option 1. Pass only a current Windows OS UA.')

    @model_validator(mode='after')
    def validate_amazon_waf_variant(self):
        if self.challengeScript is None:
            # Option 1: visible captcha, no challenge.js involved.
            if self.websiteKey is None or self.captchaScript is None:
                raise ValueError('Expect that "websiteKey" and "captchaScript" will be filled '
                                  'when "challengeScript" is not provided (Option 1).')
            if self.context is not None or self.iv is not None:
                raise ValueError('"context" and "iv" are not used when "challengeScript" is not provided (Option 1).')
        elif self.websiteKey is None and self.captchaScript is None:
            # Option 3: invisible/challenge-only captcha.
            if self.context != '' or self.iv != '':
                raise ValueError('Expect that "context" and "iv" will be empty strings '
                                  'when only "challengeScript" is provided (Option 3).')
        else:
            # Option 2: challenge + captcha.
            if self.websiteKey is None or self.context is None or self.iv is None:
                raise ValueError('Expect that "websiteKey", "context" and "iv" will be filled '
                                  'when "challengeScript" is provided together with "websiteKey" (Option 2).')
        return self

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        if self.challengeScript is not None:
            task['challengeScript'] = self.challengeScript
        if self.captchaScript is not None:
            task['captchaScript'] = self.captchaScript
        if self.websiteKey is not None:
            task['websiteKey'] = self.websiteKey
        if self.context is not None:
            task['context'] = self.context
        if self.iv is not None:
            task['iv'] = self.iv

        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword

        if self.cookieSolution is not None:
            task['cookieSolution'] = self.cookieSolution
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task