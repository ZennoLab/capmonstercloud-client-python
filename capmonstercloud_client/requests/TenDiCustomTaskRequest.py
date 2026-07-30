from typing import Dict, Optional, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class TenDiCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='TenDI')
    websiteKey: str = Field()
    metadata: Optional[Dict[str, str]] = Field(default=None)

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value is not None:
            if not set(value.keys()).issubset(set(["captchaUrl"])):
                raise TypeError(f'Allowed keys for metadata are "captchaUrl"')
            if value.get('captchaUrl') is not None and not isinstance(value.get('captchaUrl'), str):
                raise TypeError(f'Expect that captchaUrl will be str.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.metadata is not None:
            task['metadata'] = self.metadata
        return task