from typing import Dict, Optional, Union
from pydantic import Field, field_validator

from .CustomTaskRequestBase import CustomTaskRequestBase

ALLOWED_METADATA_KEYS = {
    'sceneId', 'prefix', 'userId', 'userUserId', 'verifyType',
    'region', 'UserCertifyId', 'apiGetLib', 'cookieRequired',
}

class AlibabaCustomTaskRequest(CustomTaskRequestBase):
    """
    Represents a payload structure for solving Alibaba custom captcha challenges.

    Attributes:
        captchaClass: The constant string value identifying the captcha
            class as "alibaba".
        metadata: A dictionary of Alibaba-specific parameters. Requires sceneId
            and prefix; userId, userUserId, verifyType, region, UserCertifyId,
            apiGetLib, and cookieRequired are optional, needed only for sites
            that use them.
    """
    captchaClass: str = Field(default='alibaba', description='The constant string value identifying the captcha class as "alibaba".')
    metadata: Dict[str, Union[str, bool]] = Field(..., description='A dictionary of Alibaba-specific parameters. Requires sceneId and prefix; userId, userUserId, verifyType, region, UserCertifyId, apiGetLib, and cookieRequired are optional, needed only for sites that use them.')

    @field_validator('metadata')
    @classmethod
    def validate_metadata(cls, value):
        if not set(value.keys()).issubset(ALLOWED_METADATA_KEYS):
            raise TypeError(f'Allowed keys for metadata are {sorted(ALLOWED_METADATA_KEYS)}')
        if value.get('sceneId') is None:
            raise TypeError(f'Expect that sceneId will be defined.')
        else:
            if not isinstance(value.get('sceneId'), str):
                raise TypeError(f'Expect that sceneId will be str.')
        if value.get('prefix') is None:
            raise TypeError(f'Expect that prefix will be defined.')
        else:
            if not isinstance(value.get('prefix'), str):
                raise TypeError(f'Expect that prefix will be str.')
        if value.get('cookieRequired') is not None and not isinstance(value.get('cookieRequired'), bool):
            raise TypeError(f'Expect that cookieRequired will be bool.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['metadata'] = self.metadata
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
