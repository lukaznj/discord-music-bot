import re
from re import Pattern
from discord import Embed, Colour, Interaction

from song import Song


def seconds_to_mmss(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"


def is_url(string: str) -> bool:
    # Regular expression to check if the string is a URL
    url_pattern: Pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$')
    return bool(url_pattern.match(string))
