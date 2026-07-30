from pydantic import BaseModel, field_validator
from .enums import ProxyTypes
from typing import Optional

class ProxyInfo(BaseModel):
    proxyType: str 
    proxyAddress: str
    proxyPort: int
    proxyLogin: str
    proxyPassword: str

    @field_validator('proxyType')
    @classmethod
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'Expected that proxy type will be in {ProxyTypes.list_values()}, got "{value}"')
        return value
    
    @field_validator('proxyPort')
    @classmethod
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Expect that port value will be <int> type, got {type(value)}')
        return value

class ClientProxyInfo(BaseModel):
    proxyType: str
    proxyAddress: str
    proxyPort: int
    proxyLogin: Optional[str] = None
    proxyPassword: Optional[str] = None
    
    @field_validator('proxyType')
    @classmethod
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'Expected that proxy type will be in {ProxyTypes.list_values()}, got "{value}"')
        return value
    
    @field_validator('proxyPort')
    @classmethod
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Expect that port value will be <int> type, got {type(value)}')
        return value