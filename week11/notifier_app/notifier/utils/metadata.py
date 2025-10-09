import aiohttp
import asyncio

async def fetch_metadata(doc_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://jsonplaceholder.typicode.com/posts/{doc_id}"
        async with session.get(url) as response:
            data = await response.json()
            print(f"[METADATA] Doc {doc_id}: {data['title']}")

async def fetch_all_metadata():
    await asyncio.gather(
        fetch_metadata(1),
        fetch_metadata(2),
        fetch_metadata(3),
    )