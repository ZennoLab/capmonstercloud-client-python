from typing import Optional, List, Dict, Union
from pydantic import validator
from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError


class RecognitionComplexImageTaskRequest(ComplexImageTaskRequestBase):
    captchaClass: str = 'recognition'
    metadata: Dict[str, str]

    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('Task') is None:
            raise TaskNotDefinedError(f'Expect that Task will be defined.')
        else:
            if not isinstance(value.get('Task'), str):
                raise TypeError(f'Expect that Task will be str.')
        if not set(value.keys()).issubset(set(["Task", "TaskArgument"])):
            raise TypeError(f'Allowed keys for metadata are "Task" and "TaskArgument"')
        return value
    
    @validator('imagesBase64')
    def validate_images_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type imagesBase64 array will be <list> or <tuple>, got {type(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesBase64 array are not string: {contain_types}')
        else:
            raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
        return value
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.taskType
        task['class'] = self.captchaClass
        task['imagesBase64'] = self.imagesBase64
        task['metadata'] = self.metadata
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task