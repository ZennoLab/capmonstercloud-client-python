import base64

from pydantic import validator, Field, BaseModel
from typing import Optional, Dict, Union
from .baseRequest import BaseRequest
from .enums import TextModules

class ImageToTextRequest(BaseRequest):

    image_bytes: bytes
    type: str = "ImageToTextTask"
    module_name: Optional[str] = Field(default=None)
    threshold: Optional[int] = Field(default=None)
    case: Optional[bool] = Field(default=None)
    numeric: Optional[int] = Field(default=None)
    math: Optional[bool] = Field(default=None)

    @validator('threshold')
    def validate_threshold(cls, value):
        if value is not None:
            if value not in range(0, 101):
                raise ValueError(f"threshold must be between 1 and 100, got {value}")
        return value

    @validator('module_name')
    def validate_module_name(cls, value):
        if value is not None:
            if value not in TextModules.list_values():
                raise ValueError(f"expected that module name must be in list {TextModules.list_values()}, " \
                                 f"got '{value}'")
        return value
    
    @validator('case')
    def validate_case_type(cls, value):
        if value is not None:
            if not isinstance(value, bool):
                raise TypeError(f'Case value must be type as boolean, not {type(value)}')
        return value
    
    @validator('numeric')
    def validate_numeric_range(cls, value):
        if value is not None:
            if not value in range(0, 2):
                raise ValueError(f'numeric must be between [0, 1], got {value}')
        return value

    @validator('math')
    def validate_math_type(cls, value):
        if value is not None:
            if not isinstance(value, bool):
                raise TypeError(f'Math value must be type as boolean, not {type(value)}')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['body'] = base64.b64encode(self.image_bytes).decode('utf-8')
        if self.threshold is not None:
            task['recognizingThreshold'] = int(self.threshold)
        if self.module_name is not None:
            task['CapMonsterModule'] = self.module_name
        if self.case is not None:
            task['Case'] = self.case
        if self.numeric is not None:
            task['numeric'] = int(self.numeric)
        if self.math is not None:
            task['math'] = self.math
        return task
