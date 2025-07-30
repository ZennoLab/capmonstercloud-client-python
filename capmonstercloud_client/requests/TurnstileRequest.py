from typing import Dict, Optional, Union
from pydantic import Field, validator, model_validator
from .baseRequestWithProxy import BaseRequestWithProxy


class TurnstileRequest(BaseRequestWithProxy):
    
    type: str = Field(default="TurnstileTask")
    websiteURL: str
    websiteKey: str
    pageAction: Optional[str] = Field(default=None)
    data: Optional[str] = Field(default=None)
    pageData: Optional[str] = Field(default=None)
    userAgent: Optional[str] = Field(default=None)
    cloudflareTaskType: Optional[str] = Field(default=None)
    htmlPageBase64: Optional[str] = Field(default=None)
    apiJsUrl: Optional[str] = Field(default=None)

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
        
        if self.get('proxy') is None:
            if self.get('cloudflareTaskType') == 'cf_clearance':
                raise RuntimeError(f'You are working using queries, and you need cf_clearance cookies ' \
                        f'it is required that you need your proxies.')

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
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteURL
        task['websiteKey'] = self.websiteKey
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        if self.data is not None:
            task['data'] = self.data
        if self.pageData is not None:
            task['pageData'] = self.pageData
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.cloudflareTaskType is not None:
            task['cloudflareTaskType'] = self.cloudflareTaskType
        if self.htmlPageBase64 is not None:
            task['htmlPageBase64'] = self.htmlPageBase64
        if self.apiJsUrl is not None:
            task['apiJsUrl'] = self.apiJsUrl
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword

        return task
    