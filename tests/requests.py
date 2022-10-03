import sys

sys.path.insert(1, '..')

from capmonstercloud_client import requests

PROXY_LIST = ['proxyType', 'proxyAddress', 'proxyPort', 'proxyLogin', 'proxyPassword']
RV2KEYS = {'type': 'NoCaptchaTaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'websiteKey', 'recaptchaDataSValue', 'userAgent', 'cookies']}
RV2PKEYS = {'type': 'NoCaptchaTask', 'keys': RV2KEYS['keys'] + PROXY_LIST}
RV3KEYS = {'type': 'RecaptchaV3TaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'websiteKey', 'minScore', 'pageAction']}
RV2EKEYS = {'type': 'RecaptchaV2EnterpriseTaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'websiteKey', 'enterprisePayload', 'apiDomain']}
RV2EPKEYS = {'type': 'RecaptchaV2EnterpriseTask', 'keys': RV2EKEYS['keys']+PROXY_LIST}
FCKEYS = {'type': 'FunCaptchaTaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'funcaptchaApiJSSubdomain', 'websitePublicKey', 'data']}
FCPKEYS = {'type': 'FunCaptchaTask', 'keys': FCKEYS['keys'] + PROXY_LIST}
HCKEYS = {'type': 'HCaptchaTaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'websiteKey', 'isInvisible', 'data', 'userAgent', 'cookies']}
HCPKEYS = {'type': 'HCaptchaTask', 'keys': HCKEYS['keys'] + PROXY_LIST}
I2TKEYS = {'type': 'ImageToTextTask', 'keys': 
                  ['type', 'body', 'CapMonsterModule', 'recognizingThreshold', 'Case', 'numeric', 'math']}
GTKEYS = {'type': 'GeeTestTaskProxyless', 'keys': 
                  ['type', 'websiteURL', 'gt', 'challenge', 'geetestApiServerSubdomain', 
                   'geetestGetLib', 'userAgent']}
GTPKEYS = {'type': 'GeeTestTask', 'keys': GTKEYS['keys'] + PROXY_LIST}

def recaptcha_v2():
    request = requests.RecaptchaV2ProxylessRequest(websiteUrl='some_url',
                                                    websiteKey='sime_key',
                                                    dataSValue='sdfa',
                                                    userAgent='fasdf',
                                                    cookies='asdfsdf')
    task = request.getTaskDict()
    for key in RV2KEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert RV2KEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'{RV2KEYS.get("type")}/{task.get("type")}'

    proxy_request = requests.RecaptchaV2Request(websiteUrl='some_url',
                                                websiteKey='some_key',
                                                dataSValue='data s value',
                                                userAgent='user agent',
                                                cookies='cookies',
                                                proxy_type='http',
                                                proxy_address='address',
                                                proxy_port=8001,
                                                proxy_login='login',
                                                proxy_password='password')
    proxy_task = proxy_request.getTaskDict()
    for key in RV2PKEYS.get('keys'):
        assert proxy_task.get(key) is not None, f'Missing a key {key}'
    assert RV2PKEYS.get('type') == proxy_task.get('type'), 'dont match keys ' \
                                                    f'source: {RV2PKEYS.get("type")}, your: {proxy_task.get("type")}'
        

def recaptcha_v3():
    
    request = requests.RecaptchaV3ProxylessRequest(websiteUrl='some_url',
                                                   websiteKey='some_key',
                                                   min_score=0.2,
                                                   pageAction='asdfsfd')
    task = request.getTaskDict()
    for key in RV3KEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert RV3KEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {RV3KEYS.get("type")}, your: {task.get("type")}'
        
def recaptcha_v2_enterprise():
    request = requests.RecaptchaV2EnterpriseProxylessRequest(websiteUrl='some_url',
                                                             websiteKey='some_key',
                                                             enterprisePayload='payload',
                                                             apiDomain='asdfasdf')
    task = request.getTaskDict()
    for key in RV2EKEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert RV2EKEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {RV2EKEYS.get("type")}, your: {task.get("type")}'
    proxy_request = requests.RecaptchaV2EnterpriseRequest(websiteUrl='some_url',
                                                          websiteKey='some_key',
                                                          enterprisePayload='payload',
                                                          apiDomain='asdfasdf',
                                                          proxy_type='http',
                                                          proxy_address='address',
                                                          proxy_port=8001,
                                                          proxy_login='login',
                                                          proxy_password='password')
    proxy_task = proxy_request.getTaskDict()
    for key in RV2EPKEYS.get('keys'):
        assert proxy_task.get(key) is not None, f'Missing a key {key}'
    assert RV2EPKEYS.get('type') == proxy_task.get('type'), 'dont match keys ' \
                                                    f'source: {RV2EPKEYS.get("type")}, your: {proxy_task.get("type")}'
        
def funcaptcha():
    request = requests.FuncaptchaProxylessRequest(websiteUrl='some_url',
                                                  websitePublicKey='some_key',
                                                  funcaptchaApiJSSubdomain='domain',
                                                  data='asdfasdf')
    task = request.getTaskDict()
    for key in FCKEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert FCKEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {FCKEYS.get("type")}, your: {task.get("type")}'
    proxy_request = requests.FuncaptchaRequest(websiteUrl='some_url',
                                               websitePublicKey='some_key',
                                               funcaptchaApiJSSubdomain='domain',
                                               data='asdfasdf',
                                               proxy_type='http',
                                               proxy_address='address',
                                               proxy_port=8001,
                                               proxy_login='login',
                                               proxy_password='password')
    proxy_task = proxy_request.getTaskDict()
    for key in FCPKEYS.get('keys'):
        assert proxy_task.get(key) is not None, f'Missing a key {key}'
    assert FCPKEYS.get('type') == proxy_task.get('type'), 'dont match keys ' \
                                                    f'source: {FCPKEYS.get("type")}, your: {proxy_task.get("type")}'
        
def hcaptcha():
    request = requests.HcaptchaProxylessRequest(websiteUrl='some_url',
                                                websiteKey='some_key',
                                                is_invisible=False,
                                                data='data',
                                                user_agent='agent',
                                                cookies='cookies')
    task = request.getTaskDict()
    for key in HCKEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert HCKEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {HCKEYS.get("type")}, your: {task.get("type")}'
    proxy_request = requests.HcaptchaRequest(websiteUrl='some_url',
                                             websiteKey='some_key',
                                             is_invisible=False,
                                             data='data',
                                             user_agent='agent',
                                             cookies='cookies',
                                             proxy_type='http',
                                             proxy_address='address',
                                             proxy_port=8001,
                                             proxy_login='login',
                                             proxy_password='password')
    proxy_task = proxy_request.getTaskDict()
    for key in HCPKEYS.get('keys'):
        assert proxy_task.get(key) is not None, f'Missing a key {key}'
    assert HCPKEYS.get('type') == proxy_task.get('type'), 'dont match keys ' \
                                                 f'source: {HCPKEYS.get("type")}, your: {proxy_task.get("type")}'
        

def image2text():
    request = requests.ImageToTextRequest(image_bytes=b'123321',
                                          module_name='amazon',
                                          threshold=80,
                                          case=False,
                                          numeric=1,
                                          math=True)
    task = request.getTaskDict()
    for key in I2TKEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert I2TKEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {I2TKEYS.get("type")}, your: {task.get("type")}'

def geetest():
    request = requests.GeetestProxylessRequest(websiteUrl='some_url',
                                               gt='some_key',
                                               challenge='challenge',
                                               geetestApiServerSubdomain='api.domain',
                                               geetestGetLib='lib',
                                               user_agent='agent')
    task = request.getTaskDict()
    for key in GTKEYS.get('keys'):
        assert task.get(key) is not None, f'Missing a key {key}'
    assert GTKEYS.get('type') == task.get('type'), 'dont match keys ' \
                                                    f'source: {GTKEYS.get("type")}, your: {task.get("type")}'
    proxy_request = requests.GeetestRequest(websiteUrl='some_url',
                                            gt='some_key',
                                            challenge='challenge',
                                            geetestApiServerSubdomain='api.domain',
                                            geetestGetLib='lib',
                                            user_agent='agent',
                                            proxy_type='http',
                                            proxy_address='address',
                                            proxy_port=8001,
                                            proxy_login='login',
                                            proxy_password='password')
    proxy_task = proxy_request.getTaskDict()
    for key in GTPKEYS.get('keys'):
        assert proxy_task.get(key) is not None, f'Missing a key {key}'
    assert GTPKEYS.get('type') == proxy_task.get('type'), 'dont match keys ' \
                                                 f'source: {GTPKEYS.get("type")}, your: {proxy_task.get("type")}'

def test():
    recaptcha_v2()
    recaptcha_v3()
    recaptcha_v2_enterprise()
    funcaptcha()
    hcaptcha()
    image2text()
    geetest()

if __name__ == '__main__':
    test()