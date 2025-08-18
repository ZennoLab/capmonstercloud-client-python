import os
import time
import asyncio

from capmonstercloudclient.requests import ProsopoTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(prosopo_request) for _ in range(num_requests)]


async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(prosopo_request)) for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    prosopo_request = ProsopoTaskRequest(
        websiteUrl='https://example.com/login',
        websiteKey='5EZU3LG31uzq1Mwi8inwqxmfvFDpj7VzwDnZwj4Q3syyxBwV'
    )
    print(prosopo_request.getTaskDict())
    nums = 3

    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums))
    print(f'average execution time sync {1/((time.time()-sync_start)/nums):0.2f} resp/sec\nsolution: {sync_responses[0]}')

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums))
    print(f'average execution time async {1/((time.time()-async_start)/nums):0.2f} resp/sec\nsolution: {async_responses[0]}')
