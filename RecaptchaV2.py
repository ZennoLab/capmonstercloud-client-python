import os
import asyncio

from capmonstercloud_client import CapMonsterClient, ClientOptions
from capmonstercloud_client.requests import RecaptchaV2ProxylessRequest

async def get_result():
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(recaptcha2request)) for _ in range(1)]
    return await asyncio.gather(*tasks, return_exceptions=True)
    

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
                                                    websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd")
    responses = asyncio.run(get_result())
    print(responses)