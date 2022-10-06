from typing import Optional, Union, Dict
from pydantic import Field, validator
from .baseRequest import BaseRequest


class RecaptchaV3ProxylessRequest(BaseRequest):
    websiteUrl: str 
    websiteKey: str
    type: str = Field(default='RecaptchaV3TaskProxyless')
    min_score: Optional[float] = Field(default=None)
    pageAction: Optional[str] = Field(default=None)

    @validator('min_score')
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
        if self.min_score is not None:
            task['minScore'] = self.min_score
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        return task