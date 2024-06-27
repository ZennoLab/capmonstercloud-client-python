from typing import Dict, Union
from pydantic import Field, validator

from .TenDiCustomTaskRequestBase import TenDiCustomTaskRequestBase

class TenDiCustomTaskProxylessRequest(TenDiCustomTaskRequestBase):
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task