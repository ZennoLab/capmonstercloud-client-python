import os
import time
import asyncio

from capmonstercloudclient.requests import ImpervaCustomTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient
import json

async def solve_captcha_sync(num_requests):
    return [await cap_monster_client.solve_captcha(imperva_request) for _ in range(num_requests)]

async def solve_captcha_async(num_requests):
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(imperva_request)) 
             for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    from capmonstercloudclient.requests import ProxyInfo
    proxy = ProxyInfo(
        proxyType="http",
        proxyAddress="8.8.8.8",
        proxyPort=8000,
        proxyLogin="proxyLoginHere",
        proxyPassword="proxyPasswordHere"
    )
    metadata = {"incapsulaScriptUrl": "_Incapsula_Resource?SWJIYLWA=719d34d31c8e3a6e6fffd425f7e032f3",
			"incapsulaCookie": "incap_ses_1166_2930313=br7iX33ZNCtf3HlpEXcuEDzz72cAAAAA0suDnBGrq/iA0J4oERYzjQ==; visid_incap_2930313=P3hgPVm9S8Oond1L0sXhZqfK72cAAAAAQUIPAAAAAABoMSY9xZ34RvRseJRiY6s+;",
			"reese84UrlEndpoint": "Built-with-the-For-hopence-Hurleysurfecting-the-"}
    imperva_request = ImpervaCustomTaskRequest(
        websiteUrl='https://example.com/login',
        metadata=metadata,
        proxy=proxy
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