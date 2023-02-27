from typing import Union


class Formatters:
    """
    Class for formatting data.
    """

    @staticmethod
    def humanbytes(
        size: Union[int, str],
    ) -> str:
        """
        Human friendly file size

        Args:
            size: The size in bytes.

        Returns:
            The size in a human friendly format.
        """
        if not size:
            return ""
        power = 2**10
        n = 0
        Dic_powerN = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
        while size > power:
            size /= power
            n += 1
        return str(round(size, 2)) + " " + Dic_powerN[n] + "B"

    @staticmethod
    def time_formatter(
        milliseconds: int,
    ) -> str:
        """
        Format time from milliseconds to hh:mm:ss

        Args:
            milliseconds: The time in milliseconds.

        Returns:
            The formatted time.
        """
        seconds, milliseconds = divmod(int(milliseconds), 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        tmp = (
            ((str(days) + "d, ") if days else "")
            + ((str(hours) + "h, ") if hours else "")
            + ((str(minutes) + "m, ") if minutes else "")
            + ((str(seconds) + "s, ") if seconds else "")
            + ((str(milliseconds) + "ms, ") if milliseconds else "")
        )
        return tmp[:-2]

    @staticmethod
    def get_time_in_seconds(time: str) -> int:
        """
        Convert time in a string format to seconds.

        Args:
            time: The time in string format with m/h/d/w/m/y.

        Returns:
            The time in seconds.
        """
        times = {
            "s": 1,
            "m": 60,
            "h": 3600,
            "d": 86400,
            "w": 604800,
            "m": 2630000,
            "y": 31536000,
        }
        return int(time[:-1]) * times[time[-1]]
