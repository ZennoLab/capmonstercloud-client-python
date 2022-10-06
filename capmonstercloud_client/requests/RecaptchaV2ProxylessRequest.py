from pydantic import Field, validator
from typing import Dict
from .RecaptchaV2RequestBase import RecaptchaV2RequestBase

class RecaptchaV2ProxylessRequest(RecaptchaV2RequestBase):
    type: str = Field(default="NoCaptchaTaskProxyless")

    @validator('*')
    def check_data(cls, value):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'Expect that type {value} will be "str", got {type(value)}')
        return value

    def getTaskDict(self) -> Dict[str, str]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey

        if self.dataSValue is not None:
           task['recaptchaDataSValue'] = self.dataSValue
        
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent

        if self.cookies is not None:
            task['cookies'] = self.cookies
        
        return task
