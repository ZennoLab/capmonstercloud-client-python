from pydantic import Field
from typing import Optional

from .baseRequest import BaseRequest

class HcaptchaRequestBase(BaseRequest):
    websiteUrl: str
    websiteKey: str
    is_invisible: Optional[bool] = Field(default=None)
    data: Optional[str] = Field(default=None)
    user_agent: Optional[str] = Field(default=None)
    cookies: Optional[str] = Field(default=None)
    fallbackToActualUA: Optional[bool] = Field(default=None)