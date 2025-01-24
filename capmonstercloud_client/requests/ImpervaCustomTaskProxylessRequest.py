from typing import Dict, Union
from pydantic import Field, validator

from .ImpervaCustomTaskRequestBase import ImpervaCustomTaskRequestBase

class ImpervaCustomTaskProxylessRequest(ImpervaCustomTaskRequestBase):
    metadata : Dict[str, str]
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('incapsulaScriptBase64') is None:
            raise TypeError(f'Expect that incapsulaScriptBase64 will be defined.')
        else:
            if not isinstance(value.get('incapsulaScriptBase64'), str):
                raise TypeError(f'Expect that incapsulaScriptBase64 will be str.')
        if value.get('incapsulaSessionCookie') is None:
            raise TypeError(f'Expect that incapsulaSessionCookie will be defined.')
        else:
            if not isinstance(value.get('incapsulaSessionCookie'), str):
                raise TypeError(f'Expect that incapsulaSessionCookie will be str.')
        if value.get('reese84UrlEndpoint') is not None and not isinstance(value.get('incapsulaSessionCookie'), str):
            raise TypeError(f'Expect that reese84UrlEndpoint will be str.')
        return value
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task