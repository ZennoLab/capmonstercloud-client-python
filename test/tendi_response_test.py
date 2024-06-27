import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import TenDiCustomTaskProxylessRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions

def get_all_keys(dictionary):
    all_values = []
    def recursive_items(dictionary):
        for key, value in dictionary.items():
            if type(value) is dict:
                all_values.append(key)
                recursive_items(value)
            else:
                all_values.append(key)
        return all_values
    return recursive_items(dictionary)

class TenDiOutsTest(unittest.TestCase):
    
    def testOuts(self):
        required_outs = ['domains', 'fingerprint', 'data', 'ticket', 'randstr']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
       
        request = TenDiCustomTaskProxylessRequest(websiteUrl='https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2F',
                                                    websiteKey='2009899766')
        result = asyncio.run(client.solve_captcha(request))
        for i in required_outs:
            self.assertTrue(i in get_all_keys(result))

            
if __name__ == '__main__':
    unittest.main()
        