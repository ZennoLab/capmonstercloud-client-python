from typing import Dict, Union
from pydantic import Field, validator
from .CustomTaskRequestBase import CustomTaskRequestBase

class DataDomeCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='DataDome')
    metadata : Dict[str, str]
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('datadomeCookie') is None:
            raise TypeError(f'Expect that datadomeCookie will be defined.')
        if value.get('captchaUrl') and value.get('htmlPageBase64'):
            raise TypeError(f'Expected only one of [captchaUrl, htmlPageBase64]')
        elif value.get('captchaUrl'):
            if not isinstance(value.get('captchaUrl'), str):
                raise TypeError(f'Expect that type imagesUrls array will be <str>, got {type(value.get("captchaUrl"))}')
            return {i: value[i] for i in value if i != 'htmlPageBase64'}
        elif value.get('htmlPageBase64'):
            if not isinstance(value.get('htmlPageBase64'), str):
                raise TypeError(f'Expect that type imagesUrls array will be <str>, got {type(value.get("htmlPageBase64"))}')
            return {i: value[i] for i in value if i != 'captchaUrl'}
        else:
            raise TypeError(f'Expected one of [captchaUrl, htmlPageBase64]')
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        task['domains'] = self.domains
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.domains is not None:
            task['domains'] = self.domains
        return task