from typing import Optional, List

from pydantic import Field

from .baseRequestWithProxy import BaseRequestWithProxy

class CustomTaskRequestBase(BaseRequestWithProxy):
    """
    Base payload structure for CustomTask-family anti-bot/WAF challenges
    (e.g. DataDome, Imperva, Basilisk, TenDI, Altcha, TSPD, HUNT, Alibaba,
    Friendly Captcha), each selected via a fixed "class" discriminator value.

    Attributes:
        captchaClass: The built-in class (subtype) discriminator identifying
            which CustomTask variant to solve (e.g. "DataDome", "Imperva", "HUNT").
        type: The constant string value identifying the task type as "CustomTask".
        websiteUrl: The URL of the webpage containing the captcha.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
        domains: A list of domains the returned cookies/solution should apply to.
    """

    captchaClass: str = Field(..., description='The built-in class (subtype) discriminator identifying which CustomTask variant to solve (e.g. "DataDome", "Imperva", "HUNT").')
    type: str = Field(default="CustomTask", description='The constant string value identifying the task type as "CustomTask".')
    websiteUrl: str = Field(..., description='Address of a webpage with captcha.')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Pass only a current Windows OS UA.')
    domains: Optional[List[str]] = Field(default=None, description='A list of domains the returned cookies/solution should apply to.')
