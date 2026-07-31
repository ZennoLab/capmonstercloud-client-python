from typing import Dict, Union, Optional
from pydantic import Field, field_validator

from .baseRequest import BaseRequest

class RecaptchaV3EnterpriseRequest(BaseRequest):
    """
    Represents a payload structure for solving reCAPTCHA v3 Enterprise challenges.

    Attributes:
        type: The constant string value identifying the task type as
            "RecaptchaV3EnterpriseTask".
        websiteUrl: The URL of the webpage containing the reCAPTCHA v3
            Enterprise challenge.
        websiteKey: The site key associated with the reCAPTCHA on the webpage.
        minScore: Minimum acceptable score for the token, in the range
            0.1-0.9. The returned token will be valid for this score threshold.
        pageAction: The action name configured for this reCAPTCHA v3
            Enterprise widget on the target website.
    """
    type: str = Field(default='RecaptchaV3EnterpriseTask', description='The constant string value identifying the task type as "RecaptchaV3EnterpriseTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the reCAPTCHA v3 Enterprise challenge.')
    websiteKey: str = Field(..., description='The site key associated with the reCAPTCHA on the webpage.')
    minScore: Optional[float] = Field(default=None, description='Minimum acceptable score for the token, in the range 0.1-0.9.')
    pageAction: Optional[str] = Field(default=None, description='The action name configured for this reCAPTCHA v3 Enterprise widget on the target website.')

    @field_validator('minScore')
    @classmethod
    def validate_min_score(cls, value):
        if value is not None:
            if not 0.1 <= value <= 0.9:
                raise ValueError(f'Minimum score value should be found in interval 0.1 - 0.9, ' \
                                 f'current "{value}".')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, float]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.minScore is not None:
            task['minScore'] = self.minScore
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        return task