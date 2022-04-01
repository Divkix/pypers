from httpx import AsyncClient
from typing import Any, Dict, Tuple

from aiohttp import ClientResponse, ClientSession


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


class AioHttp:
    """
    Class to help with the creation and handling of aiohttp requests.
    """

    @staticmethod
    async def get_json(
        link: str,
        **kwargs,
    ) -> Tuple[Dict[str, Any], ClientResponse]:
        """
        Get the JSON response from a link.

        Args:
            link: The URL to send request to.

        Returns:
            The JSON response from the link.
            The response object.
        """
        async with ClientSession() as session:
            async with session.get(link, **kwargs) as resp:
                return await resp.json(), resp

    @staticmethod
    async def get_text(
        link: str,
        **kwargs,
    ) -> Tuple[str, ClientResponse]:
        """
        Get the text response from a link.

        Args:
            link: The URL to send request to.

        Returns:
            The TEXT response from the link.
            The response object.
        """
        async with ClientSession() as session:
            async with session.get(link, **kwargs) as resp:
                return await resp.text(), resp

    @staticmethod
    async def get_raw(
        link: str,
        **kwargs,
    ) -> Tuple[bytes, ClientResponse]:
        """
        Get the raw response from a link.

        Args:
            link: The URL to send request to.

        Returns:
            The RAW response from the link.
            The response object.
        """
        async with ClientSession() as session:
            async with session.get(link, **kwargs) as resp:
                return await resp.read(), resp

    @staticmethod
    async def post_json(
        link: str,
        data: Dict[str, Any],
        **kwargs,
    ) -> Tuple[Dict[str, Any], ClientResponse]:
        """
        Post the JSON data to a link.

        Args:
            link: The URL to post request to.

        Returns:
            The JSON response from the link.
            The response object.
        """
        async with ClientSession() as session:
            async with session.post(link, json=data, **kwargs) as resp:
                return await resp.json(), resp
