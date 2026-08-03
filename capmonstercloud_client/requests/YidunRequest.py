from typing import Dict, Optional, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class YidunRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving NetEase Yidun captcha challenges.

    Attributes:
        type: The constant string value identifying the task type as "YidunTask".
        websiteUrl: The URL of the webpage containing the Yidun captcha challenge.
        websiteKey: The siteKey value associated with the Yidun widget on the webpage.
        userAgent: Browser User-Agent to emulate. Pass only a current
            Windows OS UA.
        yidunGetLib: The URL of the get lib script used by the Yidun widget,
            extracted from the page source when the default one does not apply.
        yidunApiServerSubdomain: The custom API server subdomain used by the
            Yidun widget, if the target page overrides the default one.
        challenge: Unique identifier of the current captcha. Its presence
            indicates the Enterprise/Business Yidun variant, and it is
            typically supplied together with hcg, hct, yidunGetLib, and
            yidunApiServerSubdomain.
        hcg: An additional Yidun-specific parameter (hcg) sometimes required
            by the widget to complete verification.
        hct: An additional Yidun-specific numeric parameter (hct) sometimes
            required by the widget to complete verification.
    """

    type: str = Field(default="YidunTask", description='The constant string value identifying the task type as "YidunTask".')
    websiteUrl: str = Field(..., description='The URL of the webpage containing the Yidun captcha challenge.')
    websiteKey: str = Field(..., description='The siteKey value associated with the Yidun widget on the webpage.')
    userAgent: Optional[str] = Field(default=None, description='Browser User-Agent to emulate. Pass only a current Windows OS UA.')
    yidunGetLib: Optional[str] = Field(default=None, description='The URL of the get lib script used by the Yidun widget, extracted from the page source when the default one does not apply.')
    yidunApiServerSubdomain: Optional[str] = Field(default=None, description='The custom API server subdomain used by the Yidun widget, if the target page overrides the default one.')
    challenge: Optional[str] = Field(default=None, description='Unique identifier of the current captcha. Its presence indicates the Enterprise/Business Yidun variant, and it is typically supplied together with hcg, hct, yidunGetLib, and yidunApiServerSubdomain.')
    hcg: Optional[str] = Field(default=None, description='An additional Yidun-specific parameter (hcg) sometimes required by the widget to complete verification.')
    hct: Optional[int] = Field(default=None, description='An additional Yidun-specific numeric parameter (hct) sometimes required by the widget to complete verification.')

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task["type"] = self.type
        task["websiteURL"] = self.websiteUrl
        task["websiteKey"] = self.websiteKey
        if self.userAgent is not None:
            task["userAgent"] = self.userAgent
        if self.yidunGetLib is not None:
            task["yidunGetLib"] = self.yidunGetLib
        if self.yidunApiServerSubdomain is not None:
            task["yidunApiServerSubdomain"] = self.yidunApiServerSubdomain
        if self.challenge is not None:
            task["challenge"] = self.challenge
        if self.hcg is not None:
            task["hcg"] = self.hcg
        if self.hct is not None:
            task["hct"] = self.hct
        if self.proxy:
            task["proxyType"] = self.proxy.proxyType
            task["proxyAddress"] = self.proxy.proxyAddress
            task["proxyPort"] = self.proxy.proxyPort
            task["proxyLogin"] = self.proxy.proxyLogin
            task["proxyPassword"] = self.proxy.proxyPassword

        return task
