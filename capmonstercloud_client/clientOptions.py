from pydantic import BaseModel, field_validator, Field
from .requests import ClientProxyInfo
from typing import Optional

class ClientOptions(BaseModel):
    api_key: str
    client_proxy: Optional[ClientProxyInfo] = None
    service_url: str = Field(default="https://api.capmonster.cloud")
    default_soft_id: int = Field(default=55)
    client_timeout: float = Field(default=20.0)
    

    @field_validator('api_key')
    @classmethod
    def validate_api_key(cls, value):
        if not isinstance(value, str):
            raise TypeError(f'Api Key must be <str> type, got {type(value)}')
        return value
    
    @field_validator('service_url')
    @classmethod
    def validate_service_url(cls, value):
        if not isinstance(value, str):
            raise TypeError(f'Service url must be <str> type, got {type(value)}')
        return value

    @field_validator('default_soft_id')
    @classmethod
    def validate_soft_id(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Soft id must be <int> type, got {type(value)}')
        return value
