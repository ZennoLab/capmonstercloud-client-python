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
from .FuncaptchaComplexImageTask import FunCaptchaComplexImageTaskRequest
from .GeetestProxylessRequest import GeetestProxylessRequest
from .GeetestRequest import GeetestRequest
from .TurnstileProxylessRequest import TurnstileProxylessRequest
from .TurnstileRequest import TurnstileRequest
from .HcaptchaComplexImageTask import HcaptchaComplexImageTaskRequest
from .RecaptchaComplexImageTask import RecaptchaComplexImageTaskRequest
from .baseRequest import BaseRequest
from .DataDomeCustomTaskRequest import DataDomeCustomTaskRequest
from .DataDomeCustomTaskProxylessRequest import DataDomeCustomTaskProxylessRequest
from .TenDiCustomTaskRequest import TenDiCustomTaskRequest
from .TenDiCustomTaskProxylessRequest import TenDiCustomTaskProxylessRequest
from .BasiliskCustomTaskRequest import BasiliskCustomTaskRequest
from .BasiliskCustomTaskProxylessRequest import BasiliskCustomTaskProxylessRequest
from .AmazonWafRequest import AmazonWafRequest
from .AmazonWafProxylessRequest import AmazonWafProxylessRequest

REQUESTS = ['RecaptchaV2EnterpiseRequest', 'RecaptchaV2EnterpriseProxylessRequest', 
            'RecaptchaV2ProxylessRequest', 'RecaptchaV2Request', 'RecaptchaV3ProxylessRequest',
            'ImageToTextRequest', 'FuncaptchaProxylessRequest', 'FuncaptchaRequest',
            'GeetestRequest', 'GeetestProxylessRequest', 'HcaptchaProxylessRequest',
            'HcaptchaRequest', 'DataDomeCustomTaskRequest', 'DataDomeCustomTaskProxylessRequest',
            'TenDiCustomTaskRequest', 'TenDiCustomTaskProxylessRequest', 'BasiliskCustomTaskRequest',
            'BasiliskCustomTaskProxylessRequest', 'AmazonWafRequest', 'AmazonWafProxylessRequest']
