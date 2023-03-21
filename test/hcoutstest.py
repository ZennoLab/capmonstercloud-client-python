import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import HcaptchaProxylessRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions

class HcaptchaOutsTest(unittest.TestCase):
    
    def testOuts(self):
        required_outs = ['gRecaptchaResponse', 'userAgent', 'respKey']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
        request = HcaptchaProxylessRequest(websiteUrl='https://lessons.zennolab.com/captchas/hcaptcha/?level=difficult',
                                           websiteKey='b744cfe0-50b1-455e-90ac-5e5a09ccb49f')
        result = asyncio.run(client.solve_captcha(request))
   
        for i in required_outs:
            self.assertTrue(i in list(result.keys()))
            
if __name__ == '__main__':
    unittest.main()
        