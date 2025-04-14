from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class BinanceTaskRequest(BaseRequestWithProxy):
    type: str = Field(default='BinanceTask')
    websiteKey: str = Field()
    websiteUrl: str = Field()
    validateId: str = Field()
    userAgent: Optional[str] = None

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['validateId'] = self.validateId
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
        return task