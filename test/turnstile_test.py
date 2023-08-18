import unittest
from copy import deepcopy

from pydantic import ValidationError
from capmonstercloudclient.requests import TurnstileProxylessRequest


class TurnstileResponseTest(unittest.TestCase):
    
    def test_turnstile(self,
                       ):
        required_fields = ['type',
                           'websiteURL', 
                           'websiteKey']
        request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAABUYP0XeMJF0xoy',
                                            websiteURL='http://tsmanaged.zlsupport.com',
                                            pageAction='asdgf')
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')

    def test_cloudflareTaskType_type(self):
        
        kwargs = {'websiteKey': '0x4AAAAAAADnPIDROrmt1Wwj',
                  'websiteURL': 'https://nowsecure.nl',
                  'cloudflareTaskType': '.'}
        self.assertRaises(ValidationError, TurnstileProxylessRequest,
                          **kwargs)
        
    def test_cf_clearance_inputs(self):
        
        required_fields = ['type',
                           'websiteURL', 
                           'websiteKey',
                           'cloudflareTaskType',
                           'htmlPageBase64']
        
        request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                            websiteURL='https://nowsecure.nl',
                                            cloudflareTaskType='cf_clearance',
                                            htmlPageBase64='htmlPageBase64Here',
                                            userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                            )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')
    
    def test_token_inputs(self):
        
        required_fields = ['type', 'websiteURL', 'websiteKey',
                           'pageAction', 'data', 'pageData',
                           'userAgent']
        
        request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                            websiteURL='https://nowsecure.nl',
                                            cloudflareTaskType='token',
                                            pageAction='pageAction',
                                            pageData='pageData',
                                            data='data',
                                            userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                            )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')
            
    def test_failed_cf_clearance_cases(self):
        
        base_kwargs = {'websiteKey': '0x4AAAAAAADnPIDROrmt1Wwj',
                       'websiteURL': 'https://nowsecure.nl'}
        
        # Token pipeline
        kwargs_1 = deepcopy(base_kwargs)
        kwargs_1.update({'cloudflareTaskType': 'token'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_1)
        kwargs_1.update({'pageAction': 'pageAction'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_1)
        kwargs_1.update({'pageData': 'pageData'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_1)
        kwargs_1.update({'data': 'data'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_1)
        kwargs_1.update({'userAgent': 'userAgent'})
        TurnstileProxylessRequest(**kwargs_1)
    
    def test_failed_token_cases(self):
        
        base_kwargs = {'websiteKey': '0x4AAAAAAADnPIDROrmt1Wwj',
                       'websiteURL': 'https://nowsecure.nl'}
        
        # cf_clearance pipeline
        kwargs_2 = deepcopy(base_kwargs)
        kwargs_2.update({'cloudflareTaskType': 'cf_clearance'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_2)
        kwargs_2.update({'htmlPageBase64': 'htmlPageBase64Here'})
        self.assertRaises(RuntimeError, TurnstileProxylessRequest, **kwargs_2)
        kwargs_2.update({'userAgent': 'userAgent'})
        TurnstileProxylessRequest(**kwargs_2)
        
if __name__ == '__main__':
    unittest.main()
        
        