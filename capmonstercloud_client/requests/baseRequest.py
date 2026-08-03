from typing import Dict, Union
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

class BaseRequest(BaseModel, ABC):
    """
    Represents the base payload structure shared by all CapMonster Cloud task requests.

    Attributes:
        no_cache: Intended to disable the use of previously cached solutions
            and force a fresh solve attempt when True. Currently unused: no
            subclass includes it in getTaskDict(), so it has no effect on the
            request actually sent.
        type: The constant string value identifying the task type. Subclasses
            override this with their specific task type name.
    """

    no_cache: bool = Field(default=False, description='Intended to disable the use of previously cached solutions and force a fresh solve attempt when True. Currently unused: no subclass includes it in getTaskDict(), so it has no effect on the request actually sent.')
    type: str = Field(default='', description='The constant string value identifying the task type.')
    
    @abstractmethod
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        pass