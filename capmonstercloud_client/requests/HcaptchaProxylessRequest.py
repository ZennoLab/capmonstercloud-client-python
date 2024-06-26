from typing import Dict, Union
from pydantic import Field

from .HcaptchaRequestBase import HcaptchaRequestBase


class HcaptchaProxylessRequest(HcaptchaRequestBase):
    type: str = Field(default='HCaptchaTaskProxyless')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.is_invisible is not None:
            task['isInvisible'] = self.is_invisible
        if self.data is not None:
            task['data'] = self.data
        if self.user_agent is not None:
            task['userAgent'] = self.user_agent
        if self.cookies is not None:
            task['cookies'] = self.cookies
        if self.fallbackToActualUA is not None:
            task['fallbackToActualUA'] = self.fallbackToActualUA
        return task