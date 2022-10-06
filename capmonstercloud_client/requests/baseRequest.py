from typing import Dict, Union
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

class BaseRequest(BaseModel, ABC):
    no_cache: bool = Field(default=False)

    @abstractmethod
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        pass