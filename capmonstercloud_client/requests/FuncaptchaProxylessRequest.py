from pydantic import Field
from typing import Dict, Union

from .FuncaptchaRequestBase import FuncaptchaRequestBase

class FuncaptchaProxylessRequest(FuncaptchaRequestBase):
    type: str = Field(default='FunCaptchaTaskProxyless')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websitePublicKey'] = self.websitePublicKey
        if self.funcaptchaApiJSSubdomain is not None:
            task['funcaptchaApiJSSubdomain'] = self.funcaptchaApiJSSubdomain
        if self.data is not None:
            task['data'] = self.data
        return task