from typing import Dict, Union, Optional
from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class BinanceTaskRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving Binance's custom captcha challenge.

    Attributes:
        type: The constant string value identifying the task type as "BinanceTask".
        websiteKey: The site key associated with the Binance captcha challenge.
        websiteUrl: The URL of the webpage containing the Binance captcha challenge.
        validateId: A unique identifier for the specific captcha validation
            attempt, issued by Binance for each challenge instance.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
    """
    type: str = Field(default='BinanceTask', description='The constant string value identifying the task type as "BinanceTask".')
    websiteKey: str = Field(description="The site key associated with the Binance captcha challenge.")
    websiteUrl: str = Field(description="The URL of the webpage containing the Binance captcha challenge.")
    validateId: str = Field(description="A unique identifier for the specific captcha validation attempt, issued by Binance for each challenge instance.")
    userAgent: Optional[str] = Field(default=None, description="Browser User-Agent to emulate. Pass only a current Windows OS UA.")

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