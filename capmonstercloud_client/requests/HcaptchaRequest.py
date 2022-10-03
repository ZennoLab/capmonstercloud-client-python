from pydantic import Field
from typing import Dict, Union

from .HcaptchaRequestBase import HcaptchaRequestBase
from .proxy_info import ProxyInfo

class HcaptchaRequest(HcaptchaRequestBase, ProxyInfo):
    type: str = Field(default='HCaptchaTask')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:

        task = {}       
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['proxyType'] = self.proxy_type
        task['proxyAddress'] = self.proxy_address
        task['proxyPort'] = self.proxy_port
        task['proxyLogin'] = self.proxy_login
        task['proxyPassword'] = self.proxy_password
        if self.is_invisible is not None:
            task['isInvisible'] = self.is_invisible
        if self.data is not None:
            task['data'] = self.data
        if self.user_agent is not None:
            task['userAgent'] = self.user_agent
        if self.cookies is not None:
            task['cookies'] = self.cookies

        return task