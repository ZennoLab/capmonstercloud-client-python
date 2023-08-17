from .baseRequest import BaseRequest, Field
from typing import Optional
from pydantic import validator, model_validator


class TurnstileRequestBase(BaseRequest):
    
    websiteURL: str
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
    
    @model_validator(mode='before')
    def validate_cloudflare_type_token(self):
        
        if self.get('htmlPageBase64') is None:
            if self.get('cloudflareTaskType') == 'cf_clearance':
                raise RuntimeError(f'Expect that "htmlPageBase64" will be filled ' \
                    f'when cloudflareTaskType is "cf_clearance"')
        
        if self.get('cloudflareTaskType') == 'token':
            for field in ['pageAction', 'pageData', 'data']:
                if self.get(field) is None:
                    raise RuntimeError(f'Expect that "{field}" will be filled ' \
                    f'when "cloudflareTaskType" = "token".')
        
        if self.get('cloudflareTaskType') is not None:
            if self.get('cloudflareTaskType') in ['cf_clearance', 'token']:
                if self.get('userAgent') is None:
                    raise RuntimeError(f'Expect that userAgent will be filled ' \
                        f'when cloudflareTaskType specified.')
                    
        return self
            