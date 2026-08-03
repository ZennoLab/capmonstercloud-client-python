from typing import Optional, Union, Dict
from pydantic import Field, field_validator
from .baseRequest import BaseRequest


class RecaptchaV3ProxylessRequest(BaseRequest):
    """
    Represents a payload structure for solving reCAPTCHA v3 challenges without a proxy.

    Attributes:
        websiteUrl: The URL of the webpage containing the reCAPTCHA v3 challenge.
        websiteKey: The site key associated with the reCAPTCHA on the webpage.
        type: The constant string value identifying the task type as
            "RecaptchaV3TaskProxyless".
        minScore: The minimum acceptable score for the returned token, in the
            range 0.1-0.9. Higher values request a token that appears more
            human-like to the target website.
        pageAction: The action name configured on the webpage for this
            reCAPTCHA v3 challenge, used to influence the score calculation.
        isEnterprise: Set to True to solve this reCAPTCHA v3 challenge via
            the Enterprise solver, using this same proxyless task type.
    """
    websiteUrl: str = Field(..., description='Address of a webpage with reCAPTCHA v3.')
    websiteKey: str = Field(..., description='The site key associated with the reCAPTCHA on the webpage.')
    type: str = Field(default='RecaptchaV3TaskProxyless', description='The constant string value identifying the task type as "RecaptchaV3TaskProxyless".')
    minScore: Optional[float] = Field(default=None, description='Minimum acceptable score for the returned token (0.1-0.9).')
    pageAction: Optional[str] = Field(default=None, description='Action name configured on the webpage for the reCAPTCHA v3 challenge.')
    isEnterprise: Optional[bool] = Field(default=None, description='Set to True to solve this reCAPTCHA v3 challenge via the Enterprise solver, using this same proxyless task type.')

    @field_validator('minScore')
    @classmethod
    def validate_min_score(cls, value):
        if value is not None:
            if not 0.1 <= value <= 0.9:
                raise ValueError(f'Minimum score value should be found in interval 0.1 - 0.9, ' \
                                 f'current "{value}".')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, float]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.minScore is not None:
            task['minScore'] = self.minScore
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        if self.isEnterprise is not None:
            task['isEnterprise'] = self.isEnterprise
        return task