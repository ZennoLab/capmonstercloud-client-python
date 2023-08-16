from pydantic import Field
from typing import Dict
from .TurnstileRequestBase import TurnstileRequestBase


class TurnstileProxylessRequest(TurnstileRequestBase):
    type: str = Field(default="TurnstileTaskProxyless")

    def getTaskDict(self) -> Dict[str, str]:
        
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        
        # Only on cloudflare challenge pages
        if self.cloudflareTaskType is not None:
            task['cloudflareTaskType'] = self.cloudflareTaskType
            if self.cloudflareTaskType == 'cf_clearance':
                
                # Check that this fields is filled
                for field in ['htmlPageBase64', 'data', 'pageData']:
                    if self.__getattribute__(field) is None:
                        raise RuntimeError(f'Expect that {field} will be filled ' \
                            f'when cloudflareTaskType = "{self.cloudflareTaskType}"')
                        
                task['htmlPageBase64'] = self.htmlPageBase64
                task['data'] = self.data
                task['pageData'] = self.pageData
        
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        else:
            if self.cloudflareTaskType == 'cf_clearance':
                raise RuntimeError(f'"pageAction" must be filled then ' \
                    f'cloudflareTaskType" specified as "cf_clearance".')
            
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        else:
            if self.cloudflareTaskType is not None:
                raise RuntimeError(f'"User Agent" must be filled then '\
                    f'cloudflareTaskType" specified.')
        
        return task
