from typing import Optional
from pydantic import Field

from .baseRequest import BaseRequest


class RecaptchaV2EnterpriseRequestBase(BaseRequest):
    websiteUrl: str
    websiteKey: str
    enterprisePayload: Optional[str] = Field(default=None)
    apiDomain: Optional[str] = Field(default=None)