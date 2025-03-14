import url_list
import aiohttp
import asyncio

talent_to_url = url_list.get_talents()

async def is_live_threaded():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for talent in talent_to_url:
            task = check_if_live(talent, session)
            tasks.append(task)
        await asyncio.gather(*tasks)

async def check_if_live(talent, session):
    try:
        headers = {
            'User-Agent': 'python-requests/2.32.3',  # Same as requests.get's User-Agent
        }

        async with session.get(talent['Url'], headers=headers) as response:
            if response.status != 200:
                print(f"Failed to fetch {talent['Url']}, status code: {response.status}")
                return

            text = await response.text(encoding='utf-8')

            if "tap to watch live" in text.lower():
                print(f"{talent['Name']} is live")
            else:
                print("Talent not live")

    except Exception as e:
        print(f"Error fetching {talent['Url']}: {e}")

asyncio.run(is_live_threaded())