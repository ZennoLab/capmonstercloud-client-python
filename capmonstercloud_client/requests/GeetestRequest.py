from pydantic import Field, validator
from typing import Dict, Union, Optional

from .baseRequestWithProxy import BaseRequestWithProxy


class GeetestRequest(BaseRequestWithProxy):
    type: str = Field(default='GeeTestTask')
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
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['gt'] = self.gt
        task['version'] = self.version
        
        if self.version == 3:
            if self.challenge is None:
                raise ValueError(f'Challenge value is required for 3 version Geetest.')
            task['challenge'] = self.challenge
        
        if self.version == 4:
            if self.initParameters is not None:
                task['initParameters'] = self.initParameters
                
        if self.geetestApiServerSubdomain is not None:
            task['geetestApiServerSubdomain'] = self.geetestApiServerSubdomain
        if self.geetestGetLib is not None:
            task['geetestGetLib'] = self.geetestGetLib
        if self.user_agent is not None:
            task['userAgent'] = self.user_agent
        
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        return task