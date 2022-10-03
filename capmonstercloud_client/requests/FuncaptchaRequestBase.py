from pydantic import Field
from typing import Optional

from .baseRequest import BaseRequest

class FuncaptchaRequestBase(BaseRequest):
    websiteUrl: str
    websitePublicKey: str
    funcaptchaApiJSSubdomain: Optional[str] = Field(default=None)
    data: Optional[str] = Field(default=None)