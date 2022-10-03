from pydantic import Field
from typing import Optional

from .baseRequest import BaseRequest

class GeetestRequestBase(BaseRequest):
    websiteUrl: str
    gt: str
    challenge: str 
    geetestApiServerSubdomain: Optional[str] = Field(default=None)
    geetestGetLib: Optional[str] = Field(default=None)
    user_agent: Optional[str] = Field(default=None)