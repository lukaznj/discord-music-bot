from typing import List

from discord import Embed, Colour, Interaction

from custom_types import Song
from helpers import seconds_to_mmss
from song_queue import SongQueue


def playing_now_embed(song: Song, interaction: Interaction) -> Embed:
    embed = Embed(
        title="Sad pjevam",
        colour=Colour.from_rgb(224, 33, 138)
    )
    embed.set_footer(text=f"Pustio: {interaction.user.display_name}",
                     icon_url=interaction.user.display_avatar.url if interaction.user.avatar else None)
    embed.set_thumbnail(url=song.thumbnail_url)
    embed.add_field(name="", value=f"**[{song.title}]({song.url})**", inline=False)
    embed.add_field(name="Autor", value=song.artist, inline=True)
    embed.add_field(name="Trajanje", value=seconds_to_mmss(song.length), inline=True)
    return embed


def added_to_queue_embed(song: Song, interaction: Interaction, queue_length: int) -> Embed:
    embed = Embed(
        title="Dodano u red čekanja",
        colour=Colour.from_rgb(224, 33, 138)
    )
    embed.set_footer(text=f"Dodao: {interaction.user.display_name}",
                     icon_url=interaction.user.display_avatar.url if interaction.user.avatar else None)
    embed.set_thumbnail(url=song.thumbnail_url)
    embed.add_field(name="", value=f"**[{song.title}]({song.url})**", inline=False)
    embed.add_field(name="Broj u redu", value=queue_length, inline=True)
    return embed


def show_queue_embed(song_queue: List[Song]) -> Embed:
    embed = Embed(
        title="Red čekanja",
        colour=Colour.from_rgb(224, 33, 138)
    )
    for i, song in enumerate(song_queue):
        embed.add_field(name="", value=f"**{i + 1}. [{song.title}]({song.url})**", inline=False)
        embed.add_field(name="", value=song.artist)
    return embed


def help_embed() -> Embed:
    embed = Embed(
        title="Lista naredbi",
        colour=Colour.from_rgb(224, 33, 138)
    )
    embed.add_field(name="`/pjevaj <pjesma>`", value="Pusti pjesmu ili ju dodaj u red čekanja.", inline=False)
    embed.add_field(name="`/red`", value="Prikaži red čekanja.", inline=False)
    embed.add_field(name="`/čisti`", value="Očisti red čekanja.", inline=False)
    embed.add_field(name="`/bok`", value="Izbaci me iz voice kanala.", inline=False)
    embed.add_field(name="`/pauziraj`", value="Pauziraj trenutnu pjesmu.", inline=False)
    embed.add_field(name="`/nastavi`", value="Nastavi pauziranu pjesmu pjesmu.", inline=False)
    embed.add_field(name="`/preskoči`", value="Preskoči trenutnu pjesmu.", inline=False)
    return embed
