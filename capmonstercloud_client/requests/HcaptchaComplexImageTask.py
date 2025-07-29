from typing import Dict, Union, List, Optional
from pydantic import Field, validator

from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError, ExtraParamsError

class HcaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase):
    
    captchaClass: str = Field(default='hcaptcha')
    metadata : Dict[str, str]
    exampleImageUrls: Optional[List[str]] = None
    exampleImagesBase64: Optional[List[str]] = None

    @staticmethod
    def _validate_image_array(value, field_name, max_images):
        """Helper method to validate image array"""
        if value is None:
            return value
        if not isinstance(value, (list, tuple)):
            raise TypeError(f'Expect that type {field_name} array will be <list> or <tuple>, got {type(value)}')

        if not len(value):
            if 'base64' in field_name.lower():
                raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
            else:
                raise ZeroImagesErrors(f'At least one image url expected, got {len(value)}')

        if len(value) > max_images:
            raise NumbersImagesErrors(f'Maximum number of images in list {max_images}, got {len(value)}')

        contain_types = [isinstance(x, str) for x in value]
        if not all(contain_types):
            if 'base64' in field_name.lower():
                raise TypeError(f'Next images from imagesBase64 array are not string: {contain_types}')
            else:
                raise TypeError(f'Next images from imagesUrls array are not string: {contain_types}')
        return value

    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('Task') is None:
            raise TaskNotDefinedError('Expect that task will be defined.')
        else:
            return value
    
    @validator('exampleImageUrls')
    def validate_example_image_urls(cls, value):
        return cls._validate_image_array(value, 'exampleImageUrls', 1)
    
    @validator('exampleImagesBase64')
    def validate_example_images_base64(cls, value):
        return cls._validate_image_array(value, 'exampleImagesBase64', 1)
    
    @validator('imagesUrls')
    def validate_images_urls(cls, value):
        return cls._validate_image_array(value, 'imagesUrls', 18)
    
    @validator('imagesBase64')
    def validate_images_base64(cls, value):
        return cls._validate_image_array(value, 'imagesBase64', 18)

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        
        task = {}
        task['type'] = self.taskType
        task['class'] = self.captchaClass
        
        # fill with images
        if self.imagesBase64 is None and self.imagesUrls is None:
            raise ZeroImagesErrors('Expect at least one of array(imageBase64 or imageUrls) to contain images.')
        
        if self.imagesUrls is not None:
            task['imageUrls'] = self.imagesUrls
        
        if self.imagesBase64 is not None:
            task['imagesBase64'] = self.imagesBase64
        
        task['metadata'] = self.metadata
        
        if self.exampleImageUrls and self.exampleImagesBase64:
            raise ExtraParamsError('Expect only one of [exampleImageUrls, exampleImagesBase64]')
        
        if self.exampleImageUrls is not None:
            task['exampleImageUrls'] = self.exampleImageUrls

        if self.exampleImagesBase64 is not None:
            task['exampleImagesBase64'] = self.exampleImagesBase64

        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        
        if self.websiteUrl is not None:
            task['websiteUrl'] = self.websiteUrl
        
        return task
    
