from httpx import AsyncClient


async def shorten_url(long_url: str):
    api_url = "https://tinyurl.com/api-create.php?url=" + long_url
    async with AsyncClient() as client:
        r = await client.get(api_url)
    return r.text
