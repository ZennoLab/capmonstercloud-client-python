from typing import Dict, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class ProsopoTaskRequest(BaseRequestWithProxy):
    type: str = Field(default="ProsopoTask")
    websiteUrl: str
    websiteKey: str

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task["type"] = self.type
        task["websiteURL"] = self.websiteUrl
        task["websiteKey"] = self.websiteKey
        if self.proxy:
            task["proxyType"] = self.proxy.proxyType
            task["proxyAddress"] = self.proxy.proxyAddress
            task["proxyPort"] = self.proxy.proxyPort
            task["proxyLogin"] = self.proxy.proxyLogin
            task["proxyPassword"] = self.proxy.proxyPassword

        return task
