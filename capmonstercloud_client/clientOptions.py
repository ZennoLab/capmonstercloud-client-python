from pydantic import BaseModel, validator, Field


class ClientOptions(BaseModel):
    api_key: str
    service_url: str = Field(default="https://api.capmonster.cloud")
    default_soft_id: int = Field(default=55)
    client_timeout: float = Field(default=20.0)

    @validator('api_key')
    def validate_api_key(cls, value):
        if not isinstance(value, str):
            raise TypeError(f'Api Key must be <str> type, got {type(value)}')
        return value
    
    @validator('service_url')
    def validate_service_url(cls, value):
        if not isinstance(value, str):
            raise TypeError(f'Service url must be <str> type, got {type(value)}')
        return value

    @validator('default_soft_id')
    def validate_soft_id(cls, value):
        if not isinstance(value, int):
            raise TypeError(f'Soft id must be <int> type, got {type(value)}')
        return value
