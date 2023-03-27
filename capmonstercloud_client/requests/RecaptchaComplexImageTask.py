from typing import Dict, Union, Optional
from pydantic import Field, validator

from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError

class RecaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase):
    
    metadata : Dict[str, str]
    captchaClass: str = Field(default='recaptcha')
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('Task') is None and value.get('TaskDefinition') is None:
            raise TaskNotDefinedError(f'Expect at least one of value(Task or TaskDefinition) will be filled.')
        elif value.get('Grid') is None:
            raise TaskNotDefinedError(f'Expect that "Grid" value will be filled(3x3, 4x4, 1x1).')
        else:
            return value
    
    @validator('imagesUrls')
    def validate_urls_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type imagesUrls array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 1:
                raise NumbersImagesErrors(f'Maximum numbers images in list 1, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image url expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesUrls array are not string: {contain_types}')
        return value
    
    @validator('imagesBase64')
    def validate_images_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type imagesBase64 array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 1:
                raise NumbersImagesErrors(f'Maximum numbers images in list 1, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesBase64 array are not string: {contain_types}')
        return value
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        
        task = {}
        task['type'] = self.taskType
        task['class'] = self.captchaClass
        
        # fill with images
        if self.imagesBase64 is None and self.imagesUrls is None:
            raise ZeroImagesErrors(f'Expect at least one of array(imageBase64 or imageUrls) to contain images.')
        
        if self.imagesUrls is not None:
            task["imageUrls"] = self.imagesUrls
        
        if self.imagesBase64 is not None:
            task["imagesBase64"] = self.imagesBase64
        
        task["metadata"] = self.metadata
        
        if self.userAgent is not None:
            task["userAgent"] = self.userAgent
            
        if self.websiteUrl is not None:
            task["websiteUrl"] = self.websiteUrl
        
        return task
    
    