# note how this library is inbuilt
import asyncio

async def download(url):
    print(f"Downloading {url}")
    # wait for the response
    await asyncio.sleep(5)
    # this could be any try/except
    print(f"Finished {url}")

async def main():
    await asyncio.gather(
        download("site1.com"),
        download("site2.com"),
    )

asyncio.run(main())