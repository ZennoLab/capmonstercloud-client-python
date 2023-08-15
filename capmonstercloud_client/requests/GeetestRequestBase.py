from pydantic import Field, validator
from typing import Dict, Optional

from .baseRequest import BaseRequest

class GeetestRequestBase(BaseRequest):
    websiteUrl: str
    gt: str
    challenge: Optional[str] = Field(default=None)
    version: int = Field(default=3)
    initParameters: Optional[Dict] = Field(default=None)
    geetestApiServerSubdomain: Optional[str] = Field(default=None)
    geetestGetLib: Optional[str] = Field(default=None)
    user_agent: Optional[str] = Field(default=None)
    
    @validator('version')
    def validate_version(cls, value):
        if value not in [3, 4]:
            raise ValueError(f"Geetest version could be 3 or 4, not {value}")
        return value