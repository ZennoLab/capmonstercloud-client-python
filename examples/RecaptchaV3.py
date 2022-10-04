import os
import asyncio

from capmonstercloud_client import CapMonsterClient, ClientOptions
from capmonstercloud_client.requests import RecaptchaV3ProxylessRequest

async def get_result():
    response = await cap_monster_client.solve_captcha(recaptcha2request)
    return response
    # tasks = [asyncio.create_task(cap_monster_client.solve_captcha(recaptcha2request)) for _ in range(1)]
    # return await asyncio.gather(*tasks, return_exceptions=True)
    

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    recaptcha2request = RecaptchaV3ProxylessRequest(websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v3.php?level=beta",
                                                    websiteKey="6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d8juDob",
                                                    min_score=0.9)
    
    responses = asyncio.run(get_result())
    print(responses)