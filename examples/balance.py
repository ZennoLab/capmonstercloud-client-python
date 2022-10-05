import os
import asyncio

from capmonstercloudclient import ClientOptions, CapMonsterClient

async def get_result():
    task = await cap_monster_client.get_balance()
    return task

if __name__ == '__main__':
    key = os.getenv('API_KEY')
    client_options = ClientOptions(api_key=key)
    cap_monster_client = CapMonsterClient(options=client_options)
    response = asyncio.run(get_result())
    print(response)