from typing import Dict, Union, Optional
from pydantic import Field, field_validator

from .baseRequest import BaseRequest

class RecaptchaV3EnterpriseRequest(BaseRequest):
    type: str = Field(default='RecaptchaV3EnterpriseTask')
    websiteUrl: str
    websiteKey: str
    minScore: Optional[float] = Field(default=None)
    pageAction: Optional[str] = Field(default=None)

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