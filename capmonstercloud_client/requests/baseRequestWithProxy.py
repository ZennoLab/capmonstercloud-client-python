from typing import Dict, Union, Optional
from pydantic import BaseModel, Field
from .baseRequest import BaseRequest
from .proxy_info import ProxyInfo

class BaseRequestWithProxy(BaseRequest):
    """
    Represents a base payload structure for tasks that are solved using a
    proxy server rather than CapMonster Cloud's own IP pool.

    Attributes:
        proxy: Proxy settings (type, address, port, and credentials) to route
            the captcha-solving request through a specified proxy server.
    """

    proxy: Optional[ProxyInfo] = Field(default=None, description='Proxy settings to route the request through a specified proxy server.')
