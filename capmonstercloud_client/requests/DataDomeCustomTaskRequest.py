from typing import Dict, Union
from pydantic import Field, validator
from .DataDomeCustomTaskRequestBase import DataDomeCustomTaskRequestBase
from .proxy_info import ProxyInfo

class DataDomeCustomTaskRequest(DataDomeCustomTaskRequestBase, ProxyInfo):
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
        task['proxyType'] = self.proxyType
        task['proxyAddress'] = self.proxyAddress
        task['proxyPort'] = self.proxyPort
        task['proxyLogin'] = self.proxyLogin
        task['proxyPassword'] = self.proxyPassword
        task['domains'] = self.domains
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.domains is not None:
            task['domains'] = self.domains
        return task