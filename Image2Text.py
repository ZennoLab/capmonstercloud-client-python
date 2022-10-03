import os
import asyncio

from capmonstercloud_client import ClientOptions, CapMonsterClient
from capmonstercloud_client.requests import ImageToTextRequest

async def get_result():
    # task = await cap_monster_client.solve_captcha(image_request)
    # return task
    tasks = [asyncio.create_task(cap_monster_client.solve_captcha(image_request)) for _ in range(3)]
    return await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)

    image_path = './samples/cat-1.jpg'
    with open(image_path, 'rb') as f:
        image_bytes = f.read()

    image_request = ImageToTextRequest(image_bytes=image_bytes, threshold=50, 
                                       module_name='amazon', case=True, numeric=1, math=False)
    response = asyncio.run(get_result())
    print(response)
    