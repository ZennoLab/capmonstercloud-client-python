from typing import Dict, Union, List, Optional
from pydantic import Field, validator

from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError, ExtraParamsError

class HcaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase):
    
    captchaClass: str = Field(default='hcaptcha')
    metadata : Dict[str, str]
    exampleImageUrls: Optional[List[str]] = None
    exampleImagesBase64: Optional[List[str]] = None
    
    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('Task') is None:
            raise TaskNotDefinedError(f'Expect that task will be defined.')
        else:
            return value
    
    @validator('exampleImageUrls')
    def validate_urls_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type exampleImageUrls array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 1:
                raise NumbersImagesErrors(f'Maximum number of images in list 1, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image url expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesUrls array are not string: {contain_types}')
        return value
    
    @validator('exampleImagesBase64')
    def validate_urls_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type exampleImagesBase64 array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 1:
                raise NumbersImagesErrors(f'Maximum number of images in list 1, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesBase64 array are not string: {contain_types}')
        return value
    
    @validator('imagesUrls')
    def validate_urls_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type imagesUrls array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 18:
                raise NumbersImagesErrors(f'Maximum number of images in list 18, got {len(value)}')
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
            elif len(value) > 18:
                raise NumbersImagesErrors(f'Maximum number of images in list 18, got {len(value)}')
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
    
    