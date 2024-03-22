from typing import Dict, Union
from pydantic import Field

from .CustomTaskRequestBase import CustomTaskRequestBase

class DataDomeCustomTaskRequestBase(CustomTaskRequestBase):
    type: str = Field(default='CustomTask')
    captchaClass: str = Field(default='DataDome')