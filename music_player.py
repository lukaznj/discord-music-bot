import os
from asyncio import sleep
from typing import Final

from discord import VoiceClient, Interaction, FFmpegPCMAudio
from dotenv import load_dotenv

from custom_types import Song
from embeds import playing_now_embed
from song_queue import SongQueue

load_dotenv()
FFMPEG_PATH: Final[str] = os.getenv("FFMPEG_PATH")


class MusicPlayer:
    def __init__(self):
        self.voice_client: VoiceClient = None
        self.queue: SongQueue = SongQueue()
        self.is_paused: bool = False

    def pause(self) -> bool:
        if not self.is_paused:
            self.voice_client.pause()
            self.is_paused = True
            return True

    def resume(self) -> bool:
        if self.is_paused:
            self.voice_client.resume()
            self.is_paused = False
            return True

    def disconnect(self) -> bool:
        if self.voice_client:
            self.voice_client.disconnect(force=True)
            return self.handle_disconnected()

    def handle_disconnected(self) -> bool:
        for song in self.queue.get_queue():
            if os.path.exists(song.file_path):
                os.remove(song.file_path)
        self.queue.clear()
        self.voice_client = None
        return True

    def is_paused(self) -> bool:
        return self.is_paused

    async def play(self, song: Song, interaction: Interaction) -> None:
        if self.voice_client:
            self.voice_client.play(FFmpegPCMAudio(executable=FFMPEG_PATH, source=song.file_path))
            await interaction.followup.send(embed=playing_now_embed(song=song, interaction=interaction))

            while self.voice_client.is_playing() or self.is_paused:
                await sleep(0.1)

            if os.path.exists(song.file_path) and self.__check_safe_delete(song):
                os.remove(song.file_path)

    def __check_safe_delete(self, song: Song) -> bool:
        for song_in_queue in self.queue.get_queue():
            if song_in_queue.file_path == song.file_path:
                return False
        return True
