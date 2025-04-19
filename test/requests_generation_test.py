import unittest

from capmonstercloudclient import requests


PROXY_LIST = ['proxyType', 'proxyAddress', 'proxyPort', 'proxyLogin', 'proxyPassword']

class RequestGenerationTests(unittest.TestCase):

    def test_rcv2(self):
        
        default_keys = ['type', 
                        'websiteURL', 
                        'websiteKey', 
                        'recaptchaDataSValue', 
                        'userAgent', 
                        'cookies']
        rc2_no_proxy_type = 'NoCaptchaTask'
        request = requests.RecaptchaV2Request(websiteUrl='some_url',
                                                       websiteKey='sime_key',
                                                       dataSValue='sdfa',
                                                       userAgent='fasdf',
                                                       cookies='asdfsdf')
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), msg=f'Missing {key} for ReCaptchaV2 request.')
        self.assertTrue(rc2_no_proxy_type==task.get('type'), 
                        msg=f'Task type of ReCaptchaV2 not equal to {rc2_no_proxy_type}')

        rc2_proxy_type = 'NoCaptchaTask'
        default_proxy_keys = default_keys + PROXY_LIST
        proxy_request = requests.RecaptchaV2Request(
            websiteUrl='some_url', websiteKey='some_key',
            dataSValue='data s value', userAgent='user agent',
            cookies='cookies', proxyType='http', proxyAddress='address',
            proxyPort=8001, proxyLogin='login', proxyPassword='password')
        proxy_task = proxy_request.getTaskDict()
        for key in default_proxy_keys:
            self.assertIsNotNone(proxy_task.get(key), msg=f'Missing {key} for ReCaptchaV2 request.')
        self.assertTrue(rc2_proxy_type==proxy_task.get('type'),     
                        msg=f'Task type of ReCaptchaV2 not equal to {rc2_proxy_type}')
        
    def test_rcv3(self):
        default_keys = ['type', 'websiteURL', 'websiteKey', 'minScore', 'pageAction']
        rc3_type = 'RecaptchaV3Task'
        request = requests.RecaptchaV3Request(websiteUrl='some_url',
                                                       websiteKey='some_key',
                                                       min_score=0.2,
                                                       pageAction='asdfsfd')
        task = request.getTaskDict()
        
        for key in default_keys:
            self.assertIsNotNone(task.get(key), msg=f'Missing {key} for ReCaptchaV3 request.')
        
        self.assertEqual(rc3_type, task.get('type'), 
                         msg=f'Task type of ReCaptchaV3 not equal to {rc3_type}')
        
    def test_rcv2_enterprise(self):
        
        rcv2e_type = 'RecaptchaV2EnterpriseTask'
        default_keys = ['type', 'websiteURL', 'websiteKey', 'enterprisePayload', 'apiDomain']
        request = requests.RecaptchaV2EnterpriseRequest(websiteUrl='some_url',
                                                                 websiteKey='some_key',
                                                                 enterprisePayload='payload',
                                                                 apiDomain='asdfasdf')
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), msg=f'Missing {key} for RecaptchaV2EnterpriseTask request.')
        self.assertEqual(rcv2e_type, task.get('type'), 
                         msg=f'Task type of RecaptchaV2EnterpriseTask not equal to {rcv2e_type}')

        proxy_request = requests.RecaptchaV2EnterpriseRequest(
            websiteUrl='some_url', websiteKey='some_key',
            enterprisePayload='payload', apiDomain='asdfasdf',
            proxyType='http', proxyAddress='address',
            proxyPort=8001, proxyLogin='login', proxyPassword='password')
        
        proxy_keys = default_keys + PROXY_LIST
        proxy_type = 'RecaptchaV2EnterpriseTask'
        proxy_task = proxy_request.getTaskDict()
        for key in proxy_keys:
            self.assertIsNotNone(proxy_task.get(key), 
                                 msg=f'Missing {key} for RecaptchaV2EnterpriseTask request.')
        self.assertEqual(proxy_type, proxy_task.get('type'), 
                         msg=f'Task type of RecaptchaV2EnterpriseTask not equal to {proxy_type}')
        
    def test_fc(self):
        noproxy_type = 'FunCaptchaTask'
        default_keys = ['type', 'websiteURL', 'funcaptchaApiJSSubdomain', 'websitePublicKey', 'data']
        request = requests.FuncaptchaRequest(websiteUrl='some_url',
                                                      websitePublicKey='some_key',
                                                      funcaptchaApiJSSubdomain='domain',
                                                      data='asdfasdf')
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), 
                                 msg=f'Missing {key} for FunCaptchaTask request.')
        self.assertEqual(noproxy_type, task.get('type'), 
                         msg=f'Task type of FunCaptchaTask not equal to {noproxy_type}')
        
        proxy_type = 'FunCaptchaTask'
        proxy_keys = default_keys + PROXY_LIST
        proxy_request = requests.FuncaptchaRequest(
            websiteUrl='some_url', websitePublicKey='some_key',
            funcaptchaApiJSSubdomain='domain', data='asdfasdf',
            proxyType='http', proxyAddress='address',
            proxyPort=8001, proxyLogin='login', proxyPassword='password')
        
        proxy_task = proxy_request.getTaskDict()
        for key in proxy_keys:
            self.assertIsNotNone(proxy_task.get(key), 
                                 msg=f'Missing {key} for FunCaptchaTask request.')
        self.assertEqual(proxy_type, proxy_task.get('type'), 
                         msg=f'Task type of FunCaptchaTask not equal to {noproxy_type}')
        
    def test_hc(self):
        
        noproxy_type = 'HCaptchaTask'
        default_keys = ['type', 'websiteURL', 'websiteKey', 'isInvisible', 'data', 'userAgent', 'cookies']
        request = requests.HcaptchaRequest(websiteUrl='some_url',
                                                    websiteKey='some_key',
                                                    is_invisible=False,
                                                    data='data',
                                                    user_agent='agent',
                                                    cookies='cookies')
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), 
                                 msg=f'Missing {key} for HCaptchaTask request.')
        self.assertEqual(noproxy_type, task.get('type'), 
                         msg=f'Task type of HCaptchaTask not equal to {noproxy_type}')
        
        proxy_request = requests.HcaptchaRequest(
            websiteUrl='some_url', websiteKey='some_key',
            is_invisible=False, data='data', user_agent='agent',
            cookies='cookies', proxyType='http', proxyAddress='address',
            proxyPort=8001, proxyLogin='login', proxyPassword='password')

        proxy_type = 'HCaptchaTask'
        proxy_keys = default_keys + PROXY_LIST
        proxy_task = proxy_request.getTaskDict()
        for key in proxy_keys:
            self.assertIsNotNone(proxy_task.get(key), 
                                 msg=f'Missing {key} for HCaptchaTask request.')
        self.assertEqual(proxy_type, proxy_task.get('type'), 
                         msg=f'Task type of HCaptchaTask not equal to {proxy_type}')
        

    def test_image2text(self):
        noproxy_type = 'ImageToTextTask'
        default_keys = ['type', 'body', 'CapMonsterModule', 
                        'recognizingThreshold', 'Case', 'numeric', 'math']
        request = requests.ImageToTextRequest(image_bytes=b'123321',
                                              module_name='amazon',
                                              threshold=80,
                                              case=False,
                                              numeric=1,
                                              math=True)
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), 
                                 msg=f'Missing {key} for ImageToTextTask request.')
        self.assertEqual(noproxy_type, task.get('type'), 
                         msg=f'Task type of ImageToTextTask not equal to {noproxy_type}')

    def test_gt(self):
        
        noproxy_type = 'GeeTestTask'
        default_keys = ['type', 'websiteURL', 'gt', 
                        'challenge', 'geetestApiServerSubdomain', 
                        'geetestGetLib', 'userAgent']
        request = requests.GeetestRequest(websiteUrl='some_url',
                                                   gt='some_key',
                                                   challenge='challenge',
                                                   geetestApiServerSubdomain='api.domain',
                                                   geetestGetLib='lib',
                                                   user_agent='agent')
        task = request.getTaskDict()
        for key in default_keys:
            self.assertIsNotNone(task.get(key), 
                                 msg=f'Missing {key} for GeeTestTask request.')
        self.assertEqual(noproxy_type, task.get('type'), 
                         msg=f'Task type of GeeTestTask not equal to {noproxy_type}')

        proxy_request = requests.GeetestRequest(
            websiteUrl='some_url', gt='some_key', challenge='challenge',
            geetestApiServerSubdomain='api.domain', geetestGetLib='lib',
            user_agent='agent', proxyType='http', proxyAddress='address',
            proxyPort=8001, proxyLogin='login', proxyPassword='password')
        proxy_task = proxy_request.getTaskDict()
        proxy_type = 'GeeTestTask'
        proxy_keys = default_keys + PROXY_LIST
        for key in proxy_keys:
            self.assertIsNotNone(proxy_task.get(key), 
                                 msg=f'Missing {key} for GeeTestTask request.')
        self.assertEqual(proxy_type, proxy_task.get('type'), 
                         msg=f'Task type of GeeTestTask not equal to {proxy_type}')

if __name__ == '__main__':
    unittest.main()