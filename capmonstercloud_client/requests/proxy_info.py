from pydantic import BaseModel, validator
from .enums import ProxyTypes

class ProxyInfo(BaseModel):
    proxyType: str 
    proxyAddress: str
    proxyPort: int
    proxyLogin: str
    proxyPassword: str

    @validator('proxyType')
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'Expected that proxy type will be in {ProxyTypes.list_values()}, got "{value}"')
        return value
    
    @validator('proxyPort')
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Expect that port value will be <int> type, got {type(value)}')
        return value
