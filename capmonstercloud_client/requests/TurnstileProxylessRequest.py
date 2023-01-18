from pydantic import Field
from typing import Dict
from .TurnstileRequestBase import TurnstileRequestBase


class TurnstileProxylessRequest(TurnstileRequestBase):
    type: str = Field(default="TurnstileTaskProxyless")

    def getTaskDict(self) -> Dict[str, str]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
