from typing import Optional, List

from .baseRequestWithProxy import BaseRequestWithProxy

class CustomTaskRequestBase(BaseRequestWithProxy):
    captchaClass: str # Class(subtype) of ComplexImageTask
    type: str = "CustomTask" # Recognition task type
    websiteUrl: str # Address of a webpage with captcha
    userAgent: Optional[str] = None # It is required that you use a signature of a modern browser
    domains: Optional[List[str]] = None # Collection with base64 encoded images. Must be populated if <see cref="ImageUrls"/> not.
