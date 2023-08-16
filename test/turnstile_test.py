import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import TurnstileProxylessRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


def solve(client: CapMonsterClient, request: TurnstileProxylessRequest):
    return asyncio.run(client.solve_captcha(request))

class TurnstileResponseTest(unittest.IsolatedAsyncioTestCase):
    
    api_key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=api_key)
    cap_monster_client = CapMonsterClient(options=client_options)
    
    def test_turnstile(self,
                       ):
        required_fields = ['type',
                           'websiteURL', 
                           'websiteKey']
        request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAABUYP0XeMJF0xoy',
                                            websiteUrl='http://tsmanaged.zlsupport.com')
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')

        
    def test_cloudflare_fields_request(self,
                        ):
        
        required_fields = ['type',
                           'websiteURL', 
                           'websiteKey',
                           'cloudflareTaskType',
                           'htmlPageBase64',
                           'data',
                           'pageData',
                           'pageAction']
        
        request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                            websiteUrl='https://nowsecure.nl',
                                            cloudflareTaskType='cf_clearance',
                                            htmlPageBase64='htmlPageBase64Here',
                                            pageData='pageDataHere',
                                            data='dataHere',
                                            pageAction='pageActionHere',
                                            userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                            )
        task_dictionary = request.getTaskDict()
        for f in required_fields:
            self.assertTrue(f in list(task_dictionary.keys()), 
                            msg=f'Required captcha input key "{f}" does not include to request.')
            
    def test_failed_request(self):
        failed_1 = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                             websiteUrl='https://nowsecure.nl',
                                             cloudflareTaskType='cf_clearance',
                                             htmlPageBase64='htmlPageBase64Here',
                                             pageData='pageDataHere',
                                             data='dataHere',
                                             pageAction='pageActionHere',
                                             )
        
        failed_2 = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                             websiteUrl='https://nowsecure.nl',
                                             cloudflareTaskType='cf_clearance',
                                             htmlPageBase64='htmlPageBase64Here',
                                             pageData='pageDataHere',
                                             data='dataHere',
                                             userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                             )
        
        failed_3 = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                             websiteUrl='https://nowsecure.nl',
                                             cloudflareTaskType='cf_clearance',
                                             htmlPageBase64='htmlPageBase64Here',
                                             pageData='pageDataHere',
                                             pageAction='pageActionHere',
                                             userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                             )
        
        failed_3 = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                             websiteUrl='https://nowsecure.nl',
                                             cloudflareTaskType='cf_clearance',
                                             htmlPageBase64='htmlPageBase64Here',
                                             data='dataHere',
                                             pageAction='pageActionHere',
                                             userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                             )
        
        failed_4 = TurnstileProxylessRequest(websiteKey='0x4AAAAAAADnPIDROrmt1Wwj',
                                             websiteUrl='https://nowsecure.nl',
                                             cloudflareTaskType='cf_clearance',
                                             pageData='pageDataHere',
                                             data='dataHere',
                                             pageAction='pageActionHere',
                                             userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.' \
                                                '0.0.0 Safari/537.36',
                                             )
        for failed_request in [failed_1, failed_2,
                               failed_3, failed_4]:
            self.assertRaises(RuntimeError, failed_request.getTaskDict)
    
    def test_cloudfare_type(self):
        kwargs = {'websiteKey' : '0x4AAAAAAADnPIDROrmt1Wwj',
                  'websiteUrl': 'https://nowsecure.nl',
                  'cloudflareTaskType': '.'}
        self.assertRaises(ValidationError, TurnstileProxylessRequest, **kwargs)
    
    # def test_turnstile_response(self):
    #     request = TurnstileProxylessRequest(websiteKey='0x4AAAAAAABUYP0XeMJF0xoy',
    #                                         websiteUrl='http://tsmanaged.zlsupport.com')
    #     response = solve(self.cap_monster_client, request)
        
        
        
if __name__ == '__main__':
    unittest.main()
        
        