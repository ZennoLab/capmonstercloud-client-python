from typing import Dict, Union
from pydantic import Field

from .CustomTaskRequestBase import CustomTaskRequestBase

class ImpervaCustomTaskRequestBase(CustomTaskRequestBase):
    type: str = Field(default='CustomTask')
    captchaClass: str = Field(default='Imperva')
