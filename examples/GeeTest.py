import os
import asyncio

from capmonstercloud_client.requests import GeetestProxylessRequest
from capmonstercloud_client import ClientOptions, CapMonsterClient

async def get_result():
    task = await cap_monster_client.solve_captcha(geetest_request)
    return task

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    geetest_request = GeetestProxylessRequest(websiteUrl='https://rucaptcha.com/demo/geetest',
                                              gt='81388ea1fc187e0c335c0a8907ff2625',
                                              challenge='e72cbf52f5749a9cfefbf92fbdaee2ea',
                                            #   geetestApiServerSubdomain='https://api.geetest.com/get.php'
                                             )
    response = asyncio.run(get_result())
    print(response)