from typing import Dict, Union, Optional
from pydantic import BaseModel, Field
from .baseRequest import BaseRequest
from .proxy_info import ProxyInfo

class BaseRequestWithProxy(BaseRequest):
    proxy: Optional[ProxyInfo] = None
