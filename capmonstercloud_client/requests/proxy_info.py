from pydantic import BaseModel, validator
from .enums import ProxyTypes

class ProxyInfo(BaseModel):
    proxy_type: str 
    proxy_address: str
    proxy_port: int
    proxy_login: str
    proxy_password: str

    @validator('proxy_type')
    def validate_proxy_type(cls, value):
        if value not in ProxyTypes.list_values():
            raise ValueError(f'Expected that proxy type will be in {ProxyTypes.list_values()}, got "{value}"')
        return value
    
    @validator('proxy_port')
    def validate_port(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Expect that port value will be <int> type, got {type(value)}')
        return value
