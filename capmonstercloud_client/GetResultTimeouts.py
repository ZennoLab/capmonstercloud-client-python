from typing import Union
from dataclasses import dataclass

@dataclass
class GetResultTimeouts:
    firstRequestDelay: Union[int, float]
    firstRequestNoCacheDelay: Union[int, float]
    requestsInterval: Union[int, float] 
    timeout: Union[int, float]

def getRecaptchaV2Timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)

def getRecaptchaV2EnterpriseTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)

def getRecaptchaV3Timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)

def getImage2TextTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(0.35, 0, 0.2, 10)

def getFuncaptchaTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 1, 80)

def getHcaptchaTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)

def getGeetestTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)

def getTurnstileTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)

def getDatadomeTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)

def getTenDiTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)

def getBasiliskTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 100)

def getAmazonWafTimeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)
