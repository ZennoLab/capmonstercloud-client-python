import unittest
import asyncio
import os

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import DataDomeCustomTaskProxylessRequest
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

class DataDomeOutsTest(unittest.TestCase):
    
    def testOuts(self):
        required_outs = ['domains', 'datadome', 'cookies']
        api_key = os.getenv('API_KEY')
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options)
        metadata =  {'captchaUrl': 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAJxx4dfgwjzwAQW0ctQ%3D%3D&hash=D66B23AC3F48A302A7654416846381&cid=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh&t=fe&referer=https%3A%2F%2Fantoinevastel.com%2Fbots%2Fdatadome&s=21705&e=04fc682817ba89bf8fa4b18031fa53294fa0fb7449d95c036a1986413e6dfc7d',
                        'datadomeCookie': 'datadome=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh'}

        request = DataDomeCustomTaskProxylessRequest(websiteUrl='https://antoinevastel.com/bots/datadome',
                                                    metadata=metadata)
        result = asyncio.run(client.solve_captcha(request))
   
        for i in required_outs:
            self.assertTrue(i in list(result.keys()))

            
if __name__ == '__main__':
    unittest.main()
        