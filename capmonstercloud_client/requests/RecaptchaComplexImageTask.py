from typing import Dict, List, Optional, Union
from pydantic import Field, field_validator

from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError

class RecaptchaComplexImageTaskRequest(ComplexImageTaskRequestBase):
    """
    Represents a payload structure for solving reCAPTCHA-style grid-based
    image classification challenges.

    Attributes:
        metadata: A dictionary describing the challenge. Must contain
            "Task" (English task name, e.g. "Click on traffic lights") and
            "TaskDefinition" (its technical identifier, e.g. "/m/015qff") —
            both required together — along with "Grid" (e.g. "3x3", "4x4",
            "1x1") specifying the image grid layout.
        captchaClass: The constant string identifying the captcha family
            as "recaptcha".
        imagesUrls: A collection of image URLs to be recognized. Must be
            populated if imagesBase64 is not.
    """

    metadata : Dict[str, str] = Field(..., description='Dictionary describing the challenge. Must contain "Task" and "TaskDefinition" (both required together) plus "Grid".')
    captchaClass: str = Field(default='recaptcha', description='Constant string identifying the captcha family as "recaptcha".')
    imagesUrls: Optional[List[str]] = Field(default=None, description='Collection with image urls. Must be populated if imagesBase64 is not.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if value.get('Task') is None or value.get('TaskDefinition') is None:
            raise TaskNotDefinedError(f'"Task" and "TaskDefinition" must both be filled.')
        elif value.get('Grid') is None:
            raise TaskNotDefinedError(f'"Grid" must be filled (3x3, 4x4, 1x1).')
        else:
            return value
    
    @field_validator('imagesUrls')
    @classmethod
    def validate_urls_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'imagesUrls must be <list> or <tuple>, got {type(value)}.')
            elif len(value) > 1:
                raise NumbersImagesErrors(f'Maximum numbers images in list 1, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image url expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesUrls array are not string: {contain_types}')
        return value
    
    @field_validator('imagesBase64')
    @classmethod
    def validate_images_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'imagesBase64 must be <list> or <tuple>, got {type(value)}.')
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
    
    