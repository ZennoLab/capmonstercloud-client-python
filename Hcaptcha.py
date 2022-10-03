import os
import asyncio

from capmonstercloud_client.requests import HcaptchaProxylessRequest
from capmonstercloud_client import ClientOptions, CapMonsterClient

async def get_result():
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(hcaptcha_request)) for _ in range(3)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    hcaptcha_request = HcaptchaProxylessRequest(websiteUrl='https://lessons.zennolab.com/captchas/hcaptcha/?level=difficult',
                                                websiteKey='b744cfe0-50b1-455e-90ac-5e5a09ccb49f')
    response = asyncio.run(get_result())
    print(response)