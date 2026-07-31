from typing import Dict, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class ProsopoTaskRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving Prosopo Procaptcha challenges.

    Attributes:
        type: The constant string value identifying the task type as "ProsopoTask".
        websiteUrl: The URL of the webpage containing the Prosopo challenge.
        websiteKey: The site key associated with the Prosopo captcha on the webpage.
    """

    type: str = Field(default="ProsopoTask", description='The constant string value identifying the task type as "ProsopoTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the Prosopo challenge.')
    websiteKey: str = Field(..., description='The site key associated with the Prosopo captcha on the webpage.')

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
