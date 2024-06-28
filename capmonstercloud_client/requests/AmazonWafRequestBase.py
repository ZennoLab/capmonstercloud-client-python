from pydantic import Field
from typing import Optional

from .baseRequest import BaseRequest

class AmazonWafRequestBase(BaseRequest):
    websiteUrl: str
    challengeScript: str
    captchaScript: str
    websiteKey: str
    context: str
    iv: str
    cookieSolution: Optional[bool] = Field(default=None)