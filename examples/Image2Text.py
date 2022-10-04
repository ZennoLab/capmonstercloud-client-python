import os
import time
import asyncio

from capmonstercloud_client import ClientOptions, CapMonsterClient
from capmonstercloud_client.requests import ImageToTextRequest

async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(image_request) for _ in range(num_requests)]

async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(image_request)) 
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    image_path = './images/cat-1.jpg'
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    image_request = ImageToTextRequest(image_bytes=image_bytes, threshold=50, 
                                       module_name='amazon', case=True, numeric=1, math=False)

    nums = 3

    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums))
    print(f'average execution time sync {1/((time.time()-sync_start)/3):0.2f} ' \
          f'resp/sec\nsolution: {sync_responses[0]}')

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums))
    print(f'average execution time async {1/((time.time()-async_start)/3):0.2f} ' \
          f'resp/sec\nsolution: {async_responses[0]}')
    