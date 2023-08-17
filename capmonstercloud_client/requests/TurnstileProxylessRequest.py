from pydantic import Field
from typing import Dict
from .TurnstileRequestBase import TurnstileRequestBase


class TurnstileProxylessRequest(TurnstileRequestBase):
    type: str = Field(default="TurnstileTaskProxyless")

    def getTaskDict(self) -> Dict[str, str]:
        return {k: v for k, v in self.model_dump().items() if v is not None}
