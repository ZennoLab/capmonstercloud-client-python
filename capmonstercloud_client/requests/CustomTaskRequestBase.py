from typing import Optional, List

from .baseRequestWithProxy import BaseRequestWithProxy

class CustomTaskRequestBase(BaseRequestWithProxy):
    captchaClass: str # Class(subtype) of ComplexImageTask
    type: str = "CustomTask" # Recognition task type
    websiteUrl: str # Address of a webpage with captcha
    userAgent: Optional[str] = None
    domains: Optional[List[str]] = None
