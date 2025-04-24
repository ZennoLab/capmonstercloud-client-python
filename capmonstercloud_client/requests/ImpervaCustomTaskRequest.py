from typing import Dict, Union
from pydantic import Field, validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class ImpervaCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='Imperva')
    metadata : Dict[str, str]
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('incapsulaScriptUrl') is None:
            raise TypeError(f'Expect that incapsulaScriptUrl will be defined.')
        else:
            if not isinstance(value.get('incapsulaScriptUrl'), str):
                raise TypeError(f'Expect that incapsulaScriptUrl will be str.')
        if value.get('incapsulaCookie') is None:
            raise TypeError(f'Expect that incapsulaCookie will be defined.')
        else:
            if not isinstance(value.get('incapsulaCookie'), str):
                raise TypeError(f'Expect that incapsulaCookie will be str.')
        if value.get('reese84UrlEndpoint') is not None and not isinstance(value.get('reese84UrlEndpoint'), str):
            raise TypeError(f'Expect that reese84UrlEndpoint will be str.')
        return value
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
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