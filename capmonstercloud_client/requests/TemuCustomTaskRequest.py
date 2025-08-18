from typing import Dict, Union
from pydantic import Field, validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TemuCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='Temu')
    metadata: Dict[str, str]

    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('cookie') is None:
            raise TypeError(f'Expect that cookie will be defined.')
        else:
            if not isinstance(value.get('cookie'), str):
                raise TypeError(f'Expect that cookie will be str.')
        if not set(value.keys()).issubset(set(["cookie"])):
            raise TypeError(f'Allowed keys for metadata are "cookie"')
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