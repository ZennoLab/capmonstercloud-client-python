import os
import time
import asyncio

from capmonstercloudclient.requests import DataDomeCustomTaskProxylessRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient

async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(datadome_request) for _ in range(num_requests)]

async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(datadome_request)) 
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    metadata = {'captchaUrl': 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAJxx4dfgwjzwAQW0ctQ%3D%3D&hash=D66B23AC3F48A302A7654416846381&cid=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh&t=fe&referer=https%3A%2F%2Fantoinevastel.com%2Fbots%2Fdatadome&s=21705&e=04fc682817ba89bf8fa4b18031fa53294fa0fb7449d95c036a1986413e6dfc7d',
                'datadomeCookie': 'datadome=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh'}
    datadome_request = DataDomeCustomTaskProxylessRequest(websiteUrl='https://antoinevastel.com/bots/datadome',
                                                    metadata=metadata
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