import asyncio
import os
import urllib
import base64
import time

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaComplexImageTaskRequest, ClientProxyInfo

async def solve_captcha_sync(num_requests,
                             client,
                             request):
    return [await client.solve_captcha(request) for _ in range(num_requests)]


if __name__ == '__main__':
    
    api_key = os.getenv('API_KEY')
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36."
    metadata = {
                "Task": "Click on traffic lights",
                "Grid": "3x3",
                "TaskDefinition": "/m/015qff"
                }
    imagesUrls = ["https://i.postimg.cc/yYjg75Kv/payloadtraffic.jpg"]
    client_proxy = ClientProxyInfo(
      proxyType='http',
      proxyAddress='gw-us.zengw.io', # get at https://docs.zennolab.com/zennoproxy/introduction or your own proxy
      proxyPort=8080, # get at https://docs.zennolab.com/zennoproxy/introduction or your own proxy
      proxyLogin='login', # get at https://docs.zennolab.com/zennoproxy/introduction or your own proxy
      proxyPassword='password' # get at https://docs.zennolab.com/zennoproxy/introduction or your own proxy
    )

    options = ClientOptions(api_key=api_key, client_proxy=client_proxy)
    client = CapMonsterClient(options)
    
    # urls example
    request_with_urls = RecaptchaComplexImageTaskRequest(metadata=metadata,
                                                         imagesUrls=imagesUrls)
    
    nums = 3
    
    print(' Test with urls '.center(120, '#'))
    
    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums, client, request_with_urls))
    print(f'average execution time sync {1/((time.time()-sync_start)/nums):0.2f} ' \
          f'resp/sec\nsolution: {sync_responses[0]}')

