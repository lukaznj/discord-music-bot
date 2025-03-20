from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    length: int
    url: str
    thumbnail_url: str
    file_path: str