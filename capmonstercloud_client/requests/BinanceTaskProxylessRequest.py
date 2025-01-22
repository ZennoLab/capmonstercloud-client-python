from typing import Dict, Union

from .BinanceTaskRequestBase import BinanceTaskRequestBase


class BinanceTaskProxylessRequest(BinanceTaskRequestBase):
    type: str = 'BinanceTaskProxyless'

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['validateId'] = self.validateId
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task