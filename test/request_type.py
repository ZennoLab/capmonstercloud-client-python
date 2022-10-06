import sys
import os
import asyncio

sys.path.insert(1, '..')

from capmonstercloud_client.requests import RecaptchaV2ProxylessRequest
from capmonstercloud_client import CapMonsterClient, ClientOptions

async def solve_captcha(client, request):
    response = await client.solve_captcha(request)
    return response


def client_test():
    api_key = os.getenv('API_KEY')
    options = ClientOptions(api_key=api_key)
    client = CapMonsterClient(options=options)

    # Success
    response_1 = asyncio.run(solve_captcha(client, 
                                           RecaptchaV2ProxylessRequest(websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
                                                                       websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd")))

    # Failed
    response_2 = asyncio.run(solve_captcha(client, 'hmmmm'))

client_test()



