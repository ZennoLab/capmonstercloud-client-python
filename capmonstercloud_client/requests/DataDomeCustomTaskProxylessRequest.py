from typing import Dict, Union
from pydantic import Field, validator

from .DataDomeCustomTaskRequestBase import DataDomeCustomTaskRequestBase
from ..exceptions import WrongMetadataError

class DataDomeCustomTaskProxylessRequest(DataDomeCustomTaskRequestBase):
    metadata : Dict[str, str]
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('datadomeCookie') is None:
            raise WrongMetadataError(f'Expect that datadomeCookie will be defined.')
        if value.get('captchaUrl'):
            return {i: value[i] for i in value if i != 'htmlPageBase64'}
        elif value.get('htmlPageBase64'):
            return {i: value[i] for i in value if i != 'captchaUrl'}
        else:
            raise WrongMetadataError(f'Expect that one of [captchaUrl, htmlPageBase64] will be defined.')
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['domains'] = self.domains
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.domains is not None:
            task['domains'] = self.domains
        return task