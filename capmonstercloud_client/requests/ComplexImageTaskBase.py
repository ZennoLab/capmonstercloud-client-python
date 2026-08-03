from typing import Optional, List

from pydantic import Field

from .baseRequest import BaseRequest

class ComplexImageTaskRequestBase(BaseRequest):
    """
    Represents a payload structure for solving complex image-based recognition tasks.

    Attributes:
        captchaClass: The class (subtype) of the ComplexImageTask, identifying
            the specific image recognition scenario to be solved.
        taskType: The constant string value identifying the task type as
            "ComplexImageTask".
        websiteUrl: The URL of the webpage containing the captcha, if applicable.
        imagesBase64: A collection of base64-encoded images to be recognized.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
    """
    captchaClass: str = Field(..., description='Class(subtype) of ComplexImageTask.') # Class(subtype) of ComplexImageTask
    taskType: str = Field(default="ComplexImageTask", description='Recognition task type.') # Recognition task type
    websiteUrl: Optional[str] = Field(default=None, description='Address of a webpage with captcha.') # Address of a webpage with captcha
    imagesBase64: Optional[List[str]] = Field(default=None, description='Collection with base64 encoded images.') # Collection with base64 encoded images.
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Pass only a current Windows OS UA.')