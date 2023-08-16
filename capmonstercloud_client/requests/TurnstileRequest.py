from typing import Dict
from pydantic import Field
from .TurnstileRequestBase import TurnstileRequestBase
from .proxy_info import ProxyInfo


class TurnstileRequest(TurnstileRequestBase, ProxyInfo):
    
    type: str = Field(default="TurnstileTask")

    def getTaskDict(self) -> Dict[str, str]:
        return {k: v for k, v in self.model_dump().items() if v is not None}
    