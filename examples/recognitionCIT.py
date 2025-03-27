import os
import time
import asyncio
import base64
from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient

async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(oocl_request) for _ in range(num_requests)]

async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(oocl_request)) 
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    with open("/path/to/img/0_2.png", 'rb') as f:
        bg = base64.b64encode(f.read()).decode("utf-8")
    with open("/path/to/img/0_0.png", 'rb') as f:
        ring = base64.b64encode(f.read()).decode("utf-8")
    with open("/path/to/img/0_1.png", 'rb') as f:
        circle = base64.b64encode(f.read()).decode("utf-8")
    oocl_request = RecognitionComplexImageTaskRequest(
        metadata={"Task": "oocl_rotate_double_new"},
        imagesBase64=[bg, ring, circle]
    )
    nums = 3

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