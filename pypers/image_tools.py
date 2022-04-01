from typing import Optional
from PIL import Image


class ImageTools:
    """
    Class for image manipulation
    """

    @staticmethod
    async def compress_image(
        image_path: str,
        quality: Optional[int] = 25,
    ) -> str:
        """
        Compress an image using Pillow.

        Args:
            image_path: The path to the image to compress.
            quality: The quality of the compressed image.

        Returns:
            The path to the compressed image.
        """
        image_name = image_path.split("/")[-1]
        new_filename = f"compressed_{image_name}"

        pic = Image.open(image_path)
        pic = pic.resize(pic.size, Image.LANCZOS)
        pic.save(
            new_filename,
            optimize=True,
            quality=quality,
        )
        return new_filename
