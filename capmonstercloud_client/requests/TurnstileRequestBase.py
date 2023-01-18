from .baseRequest import BaseRequest, Field
from typing import Optional


class TurnstileRequestBase(BaseRequest):
    websiteUrl: str
    websiteKey: str
    userAgent: Optional[str] = Field(default=None)