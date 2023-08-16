from typing import Dict, Union
from pydantic import Field
from .TurnstileRequestBase import TurnstileRequestBase
from .proxy_info import ProxyInfo


class TurnstileRequest(TurnstileRequestBase, ProxyInfo):
    
    type: str = Field(default="TurnstileTask")

    def getTaskDict(self) -> Dict[str, Union[str, int]]:
        
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
        
        task['proxyType'] = self.proxy_type
        task['proxyAddress'] = self.proxy_address
        task['proxyPort'] = self.proxy_port
        if self.proxy_login is not None:
            task['proxyLogin'] = self.proxy_login
        if self.proxy_password is not None:
            task['proxyPassword'] = self.proxy_password

        return task
    