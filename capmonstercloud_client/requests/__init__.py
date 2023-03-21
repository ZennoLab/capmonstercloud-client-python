from .ImageToTextRequest import ImageToTextRequest
from .RecaptchaV2ProxylessRequest import RecaptchaV2ProxylessRequest
from .RecaptchaV2Request import RecaptchaV2Request
from .RecaptchaV2EnterpriseProxylessRequest import RecaptchaV2EnterpriseProxylessRequest
from .RecaptchaV2EnterpiseRequest import RecaptchaV2EnterpriseRequest
from .RecaptchaV3ProxylessRequest import RecaptchaV3ProxylessRequest
from .HcaptchaProxylessRequest import HcaptchaProxylessRequest
from .HcaptchaRequest import HcaptchaRequest
from .FuncaptchaProxylessRequest import FuncaptchaProxylessRequest
from .FuncaptchaRequest import FuncaptchaRequest
from .GeetestProxylessRequest import GeetestProxylessRequest
from .GeetestRequest import GeetestRequest
from .TurnstileProxylessRequest import TurnstileProxylessRequest
from .TurnstileRequest import TurnstileRequest
from .HcaptchaComplexImageTask import HcaptchaComplexImageTaskRequest
from .RecaptchaComplexImageTask import RecaptchaComplexImageTaskRequest
from .baseRequest import BaseRequest

REQUESTS = ['RecaptchaV2EnterpiseRequest', 'RecaptchaV2EnterpriseProxylessRequest', 
            'RecaptchaV2ProxylessRequest', 'RecaptchaV2Request', 'RecaptchaV3ProxylessRequest',
            'ImageToTextRequest', 'FuncaptchaProxylessRequest', 'FuncaptchaRequest',
            'GeetestRequest', 'GeetestProxylessRequest', 'HcaptchaProxylessRequest',
            'HcaptchaRequest']