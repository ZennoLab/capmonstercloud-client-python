from pydantic import Field
from typing import Optional

from .baseRequest import BaseRequest


class RecaptchaV2RequestBase(BaseRequest):
    websiteUrl: str
    websiteKey: str
    dataSValue: Optional[str] = Field(default=None)
    userAgent: Optional[str] = Field(default=None)
    cookies: Optional[str] = Field(default=None)