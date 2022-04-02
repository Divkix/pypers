from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


class VideoTools:
    @staticmethod
    def extract_vid_data(output_vid: str):
        metadata = extractMetadata(createParser(output_vid))
        duration = metadata.get("duration").seconds if metadata.has("duration") else 0
        width = metadata.get("width") if metadata.has("width") else 100
        height = metadata.get("height") if metadata.has("height") else 100
        return duration, width, height
