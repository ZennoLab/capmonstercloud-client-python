from typing import Optional, List

from .baseRequest import BaseRequest

class ComplexImageTaskRequestBase(BaseRequest):
    captchaClass: str # Class(subtype) of ComplexImageTask
    taskType: str = "ComplexImageTask" # Recognition task type
    websiteUrl: Optional[str] = None # Address of a webpage with captcha
    imagesUrls: Optional[List[str]] = None # Collection with image urls. Must be populated if <see cref="ImagesBase64"/> not.
    imagesBase64: Optional[List[str]] = None # Collection with base64 encoded images. Must be populated if <see cref="ImageUrls"/> not.
    userAgent: Optional[str] = None # It is required that you use a signature of a modern browser