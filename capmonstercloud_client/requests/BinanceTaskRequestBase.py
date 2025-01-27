from .baseRequest import BaseRequest, Field
from typing import Optional


class BinanceTaskRequestBase(BaseRequest):
    
    type: str = Field(default='BinanceTask')
    websiteKey: str = Field()
    websiteUrl: str = Field()
    validateId: str = Field()
    userAgent: Optional[str] = None
