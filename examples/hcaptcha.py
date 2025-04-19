import os
import time
import asyncio

from capmonstercloudclient.requests import HcaptchaRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient

async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(hcaptcha_request) for _ in range(num_requests)]

async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(hcaptcha_request)) 
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    hcaptcha_request = HcaptchaRequest(websiteUrl='https://lessons.zennolab.com/captchas/hcaptcha/?level=difficult',
                                                websiteKey='b744cfe0-50b1-455e-90ac-5e5a09ccb49f')
    
    nums = 3
    print(hcaptcha_request.getTaskDict())
    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums))
    print(f'average execution time sync {1/((time.time()-sync_start)/nums):0.2f} ' \
          f'resp/sec\nsolution: {sync_responses[0]}')

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums))
    print(f'average execution time async {1/((time.time()-async_start)/nums):0.2f} ' \
          f'resp/sec\nsolution: {async_responses[0]}')