import asyncio
from typing import List
from discord.app_commands import Choice
from pytubefix import YouTube, Stream
from pytubefix import Search
from custom_types import Song


async def download_song(url: str) -> Song:
    yt: YouTube = YouTube(url)
    stream: Stream = max(yt.streams.filter(only_audio=True), key=lambda s: int(s.abr[:-4]))

    await asyncio.to_thread(stream.download, output_path="tmp")

    return Song(
        title=yt.title,
        artist=yt.author,
        length=yt.length,
        url=url,
        thumbnail_url=yt.thumbnail_url,
        file_path=f"tmp/{stream.default_filename}"
    )


def search(query: str) -> List[Choice]:
    results: List[YouTube] = Search(query).videos[:3]
    return [Choice(name=result.title, value=result.watch_url) for result in results]


if __name__ == "__main__":
    print(search("I MISS THE RAGE"))
