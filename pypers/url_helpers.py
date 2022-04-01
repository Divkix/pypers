from httpx import AsyncClient


class UrlHelpers:
    """
    Class to help with the creation and handling of urls
    """

    @staticmethod
    async def shorten_url(
        long_url: str,
    ) -> str:
        """
        Shorten a long URL using the tinyurl.com API.

        Args:
            long_url: The long URL to shorten.

        Returns:
            The shortened URL.
        """
        api_url = "https://tinyurl.com/api-create.php?url=" + long_url
        async with AsyncClient() as client:
            r = await client.get(api_url)
        return r.text
