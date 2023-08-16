from .baseRequest import BaseRequest, Field
from typing import Optional
from pydantic import validator


class TurnstileRequestBase(BaseRequest):
    websiteUrl: str
    websiteKey: str
    pageAction: Optional[str] = Field(default=None)
    data: Optional[str] = Field(default=None)
    pageData: Optional[str] = Field(default=None)
    userAgent: Optional[str] = Field(default=None)
    cloudflareTaskType: Optional[str] = Field(default=None)
    htmlPageBase64: Optional[str] = Field(default=None)
    
    @validator('cloudflareTaskType')
    def validate_cloudflare_task(cls, value):
        if value is not None:
            if value not in ['cf_clearance', 'token']:
                raise ValueError(f'cloudflareTaskType could be "cf_clearance" if you need cookie or ' \
                                 f'"token" if required token from Turnstile.')
        return value
            