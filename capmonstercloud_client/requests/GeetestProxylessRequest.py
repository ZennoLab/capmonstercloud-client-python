from pydantic import Field
from typing import Dict, Union

from .GeetestRequestBase import GeetestRequestBase

class GeetestProxylessRequest(GeetestRequestBase):
    type: str = Field(default='GeeTestTaskProxyless')

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
        return task