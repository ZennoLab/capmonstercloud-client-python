from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequest import BaseRequest

class RecaptchaV3EnterpriseRequest(BaseRequest):
    type: str = Field(default='RecaptchaV3EnterpriseTask')
    websiteUrl: str
    websiteKey: str
    minScore: Optional[float] = Field(default=None)
    pageAction: Optional[str] = Field(default=None)
    
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