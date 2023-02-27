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
        seconds: int,
    ) -> str:
        """
        Format time from seconds to hh:mm:ss

        Args:
            seconds: The time in seconds.

        Returns:
            The formatted time.
        """
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        tmp = (
            ((str(months) + "m, ") if months else "")
            + ((str(days) + "d, ") if days else "")
            + ((str(hours) + "h, ") if hours else "")
            + ((str(minutes) + "min, ") if minutes else "")
            + ((str(seconds) + "s, ") if seconds else "")
        )
        return tmp[:-2]

    @staticmethod
    def get_time_in_seconds(time: str) -> int:
        """
        Convert time in a string format to seconds.

        Args:
            time: The time in string format with s/m/h/d/w.

        Returns:
            The time in seconds.
        """
        time = time.lower()
        # the last char of the time, e.g. s, m, h, d, w
        time_last_chars = time[1:]
        times = {
            "s": 1,
            "m": 60,
            "h": 3600,
            "d": 86400,
            "w": 604800,
        }
        # check if the last char is in the times dict
        if time_last_chars not in times:
            return -1
        return int(time[:-1]) * times[time_last_chars]
