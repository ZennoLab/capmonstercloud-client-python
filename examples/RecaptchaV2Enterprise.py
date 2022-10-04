import os
import asyncio
from capmonstercloud_client import CapMonsterClient, ClientOptions
from capmonstercloud_client.requests import RecaptchaV2EnterpriseProxylessRequest

async def get_result():
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(recaptcha2request)) for _ in range(1)]
    return await asyncio.gather(*tasks, return_exceptions=True)
    

if __name__ == '__main__':
    steam_site = r"https://store.steampowered.com/join/?redir=%3Fsnr%3D1_60_4__global-header&snr=1_60_4__62"
    steam_key = "6LdIFr0ZAAAAAO3vz0O0OQrtAefzdJcWQM2TMYQH"
    spotify_site = r"https://www.spotify.com/fi/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    spotify_key = "6LeO36obAAAAALSBZrY6RYM1hcAY7RLvpDDcJLy3"

    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    recaptcha2request = RecaptchaV2EnterpriseProxylessRequest(websiteUrl=spotify_site,
                                                              websiteKey=spotify_key)
    responses = asyncio.run(get_result())
    print(responses)