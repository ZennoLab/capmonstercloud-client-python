from typing import Dict, Optional, Union
from pydantic import Field, field_validator, model_validator
from .baseRequestWithProxy import BaseRequestWithProxy


class TurnstileRequest(BaseRequestWithProxy):
    """
    Represents a payload structure for solving Cloudflare Turnstile challenges.

    Attributes:
        type: The constant string value identifying the task type as "TurnstileTask".
        websiteURL: The URL of the webpage containing the Turnstile challenge.
        websiteKey: The site key associated with the Turnstile widget on the webpage.
        pageAction: The action name configured for the Turnstile widget, if the
            website uses the "action" parameter to distinguish between challenges.
            Required when cloudflareTaskType is "token".
        data: The "cData" custom payload value passed to the Turnstile widget,
            required when cloudflareTaskType is "token" and the widget uses this field.
        pageData: The "chlPageData" value used by the Turnstile widget for
            interactive challenges, required when cloudflareTaskType is "token" and
            the widget uses this field.
        userAgent: The User-Agent string of the browser to emulate. Required
            whenever cloudflareTaskType is specified.
        cloudflareTaskType: The mode of the Cloudflare task: "cf_clearance" to
            obtain the cf_clearance cookie, "token" to obtain a Turnstile token, or
            "wait_room" to pass a Cloudflare waiting room.
        htmlPageBase64: The base64-encoded HTML source of the target page.
            Required when cloudflareTaskType is "cf_clearance" or "wait_room".
        apiJsUrl: The URL of the Turnstile API script (api.js) used on the page,
            if it differs from the default Cloudflare endpoint.
    """

    type: str = Field(default="TurnstileTask", description='The constant string value identifying the task type as "TurnstileTask".')
    websiteURL: str = Field(..., description='The URL of the webpage containing the Turnstile challenge.')
    websiteKey: str = Field(..., description='The site key associated with the Turnstile widget on the webpage.')
    pageAction: Optional[str] = Field(default=None, description='The action name configured for the Turnstile widget, if the website uses the "action" parameter to distinguish between challenges. Required when cloudflareTaskType is "token".')
    data: Optional[str] = Field(default=None, description='The "cData" custom payload value passed to the Turnstile widget, required when cloudflareTaskType is "token" and the widget uses this field.')
    pageData: Optional[str] = Field(default=None, description='The "chlPageData" value used by the Turnstile widget for interactive challenges, required when cloudflareTaskType is "token" and the widget uses this field.')
    userAgent: Optional[str] = Field(default=None, description='The User-Agent string of the browser to emulate. Required whenever cloudflareTaskType is specified.')
    cloudflareTaskType: Optional[str] = Field(default=None, description='The mode of the Cloudflare task: "cf_clearance" to obtain the cf_clearance cookie, "token" to obtain a Turnstile token, or "wait_room" to pass a Cloudflare waiting room.')
    htmlPageBase64: Optional[str] = Field(default=None, description='The base64-encoded HTML source of the target page. Required when cloudflareTaskType is "cf_clearance" or "wait_room".')
    apiJsUrl: Optional[str] = Field(default=None, description='The URL of the Turnstile API script (api.js) used on the page, if it differs from the default Cloudflare endpoint.')

    @field_validator('cloudflareTaskType')
    @classmethod
    def validate_cloudflare_task(cls, value):
        if value is not None:
            if value not in ['cf_clearance', 'token', 'wait_room']:
                raise ValueError(f'cloudflareTaskType could be "cf_clearance" if you need cookie or ' \
                                 f'"token" if required token from Turnstile.')
        return value
    
    @model_validator(mode='before')
    def validate_cloudflare_type_token(self):
        
        if self.get('htmlPageBase64') is None:
            if self.get('cloudflareTaskType') in ['cf_clearance', 'wait_room']:
                raise RuntimeError(f'Expect that "htmlPageBase64" will be filled ' \
                    f'when cloudflareTaskType is "cf_clearance" or "wait_room')
        
        if self.get('proxy') is None:
            if self.get('cloudflareTaskType') in ['cf_clearance', 'wait_room']:
                raise RuntimeError(f'You are working using queries, and you need cf_clearance cookies or wait_room ' \
                        f'it is required that you need your proxies.')

        if self.get('cloudflareTaskType') == 'token':
            for field in ['pageAction', 'pageData', 'data']:
                if self.get(field) is None:
                    raise RuntimeError(f'Expect that "{field}" will be filled ' \
                    f'when "cloudflareTaskType" = "token".')
        
        if self.get('cloudflareTaskType') is not None:
            if self.get('cloudflareTaskType') in ['cf_clearance', 'token', 'wait_room']:
                if self.get('userAgent') is None:
                    raise RuntimeError(f'Expect that userAgent will be filled ' \
                        f'when cloudflareTaskType specified.')
          
        return self
    
    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteURL
        task['websiteKey'] = self.websiteKey
        if self.pageAction is not None:
            task['pageAction'] = self.pageAction
        if self.data is not None:
            task['data'] = self.data
        if self.pageData is not None:
            task['pageData'] = self.pageData
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        if self.cloudflareTaskType is not None:
            task['cloudflareTaskType'] = self.cloudflareTaskType
        if self.htmlPageBase64 is not None:
            task['htmlPageBase64'] = self.htmlPageBase64
        if self.apiJsUrl is not None:
            task['apiJsUrl'] = self.apiJsUrl
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword

        return task
    