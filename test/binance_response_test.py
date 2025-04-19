import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import BinanceTaskRequest
from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests.proxy_info import ProxyInfo

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

class AmazonWafOutsTest(unittest.TestCase):
    
    def testOuts(self):
        required_outs = ['token', 'userAgent']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
        request = BinanceTaskRequest(websiteUrl='https://accounts.binance.com/ru/login?loginChannel=&return_to=',
                                             websiteKey='login',
                                             validateId="2b8137c0b9b44189800368819354e114"
                                            )
        result = asyncio.run(client.solve_captcha(request))
        for i in required_outs:
            self.assertTrue(i in get_all_keys(result))

    def testOutsProxy(self):
        required_outs = ['token', 'userAgent']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
        proxy = ProxyInfo(proxyType='https', 
                          proxyAddress='proxyAddress',
                          proxyPort=8000,
                          proxyLogin='proxyLogin',
                          proxyPassword='proxyPassword'
        )
        request = BinanceTaskRequest(websiteUrl='https://accounts.binance.com/ru/login?loginChannel=&return_to=',
                                     websiteKey='login',
                                     validateId="2b8137c0b9b44189800368819354e114",
                                     proxy=proxy
        )
        result = asyncio.run(client.solve_captcha(request))
        for i in required_outs:
            self.assertTrue(i in get_all_keys(result))
    
            
if __name__ == '__main__':
    unittest.main()
        