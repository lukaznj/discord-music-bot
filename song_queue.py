from typing import List
from custom_types import Song


class SongQueue:
    def __init__(self):
        self.queue: List[Song] = []

    def add_song(self, song: Song) -> None:
        self.queue.append(song)

    def get_next_song(self) -> Song:
        return self.queue.pop(0) if self.queue else None

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def clear(self) -> None:
        self.queue.clear()

    def length(self) -> int:
        return len(self.queue)

    def get_queue(self) -> List[Song]:
        return self.queue
