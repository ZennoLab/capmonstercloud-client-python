from typing import Dict, Union
from pydantic import Field, validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class AltchaCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='altcha')
    websiteKey: str = Field()
    metadata : Dict[str, str]
    
    @validator('metadata')
    def validate_metadata(cls, value):
        for key in ['challenge', 'iterations', 'salt', 'signature']:
            if value.get(key) is None:
                raise TypeError(f'Expect that {key} will be defined.')
            else:
                if not isinstance(value.get(key), str):
                    raise TypeError(f'Expect that {key} will be str.')
        return value
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['metadata'] = self.metadata
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
