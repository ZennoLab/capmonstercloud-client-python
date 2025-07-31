from typing import Dict, Optional, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class MTCaptchaRequest(BaseRequestWithProxy):
    type: str = Field(default="MTCaptchaTask")
    websiteUrl: str
    websiteKey: str
    pageAction: Optional[str] = Field(default=None)
    isInvisible: Optional[bool] = Field(default=None)
    userAgent: Optional[str] = Field(default=None)

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task["type"] = self.type
        task["websiteURL"] = self.websiteUrl
        task["websiteKey"] = self.websiteKey
        if self.pageAction is not None:
            task["pageAction"] = self.pageAction
        if self.isInvisible is not None:
            task["isInvisible"] = self.isInvisible
        if self.userAgent is not None:
            task["userAgent"] = self.userAgent
        if self.proxy:
            task["proxyType"] = self.proxy.proxyType
            task["proxyAddress"] = self.proxy.proxyAddress
            task["proxyPort"] = self.proxy.proxyPort
            task["proxyLogin"] = self.proxy.proxyLogin
            task["proxyPassword"] = self.proxy.proxyPassword

        return task
