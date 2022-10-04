import os
import asyncio

from capmonstercloud_client.requests import FuncaptchaProxylessRequest
from capmonstercloud_client import ClientOptions, CapMonsterClient

async def get_result():
    task = await cap_monster_client.solve_captcha(funcaptcha_request)
    return task

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    funcaptcha_request = FuncaptchaProxylessRequest(websiteUrl='https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1664627861&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d7b21be2b-b515-ed6b-b944-7008600280b4&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&lic=1&uaid=6c51fa8140d946f7b14a00b6cd6feef8',
                                                    websitePublicKey='B7D8911C-5CC8-A9A3-35B0-554ACEE604DA',
                                                    funcaptchaApiJSSubdomain='https%3A%2F%2Fclient-api.arkoselabs.com')
    response = asyncio.run(get_result())
    print(response)