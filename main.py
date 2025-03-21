import os
from discord.app_commands import Choice
from dotenv import load_dotenv
from pytubefix import Search
from song import Song
from embeds import added_to_queue_embed, show_queue_embed, help_embed
from helpers import is_url
from music_player import MusicPlayer
from pytube_engine import download_song, search
from typing import Final, List
from discord import Intents, Interaction, VoiceState, VoiceChannel, VoiceClient, VoiceProtocol
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

if not os.path.exists("tmp"):
    os.makedirs("tmp")

intents: Intents = Intents.default()
intents.message_content = True  # NOQA

bot = commands.Bot(command_prefix="!", intents=intents)

music_player = MusicPlayer()


@bot.event
async def on_ready() -> None:
    print(f"{bot.user} connected successfully.")


@bot.event
async def on_voice_state_update(member, before, after):
    if member == bot.user and before.channel is not None and after.channel is None:
        # Bot was disconnected from the voice channel by disconnect() or external means
        music_player.handle_disconnected()


@bot.tree.command(name="upomoć", description="Izlistaj sve naredbe koje mogu odraditi.")
async def help_command(interaction: Interaction) -> None:
    await interaction.response.send_message(embed=help_embed())


@bot.tree.command(name="bok", description="Pozdravi me da izađem iz voice kanala.")
async def leave_voice(interaction: Interaction) -> None:
    if music_player.disconnect():
        await interaction.response.send_message("Vidimo se!")
    else:
        await interaction.response.send_message("Nisam u voice kanalu tipane.")


@bot.tree.command(name="pauziraj", description="Pauziraj trenutnu pjesmu.")
async def pause_audio(interaction: Interaction) -> None:
    if music_player.voice_client:
        await interaction.response.send_message("Pauziram!" if music_player.pause() else "Već sam na pauzi!")
    else:
        await interaction.response.send_message("Nisam u voice kanalu tipane.")


@bot.tree.command(name="nastavi", description="Nastavi pjesmu koja je pauzirana.")
async def resume_audio(interaction: Interaction) -> None:
    if music_player.voice_client:
        await interaction.response.send_message(
            "Nastavljam!" if music_player.resume() else "Pjesma nije pauzirana.")
    else:
        await interaction.response.send_message("Nisam u voice kanalu tipane.")


@bot.tree.command(name="preskoči", description="Preskoči trenutnu pjesmu.")
async def skip_audio(interaction: Interaction) -> None:
    if music_player.voice_client:
        music_player.voice_client.stop()
        await interaction.response.send_message("Idemo dalje!")
    else:
        await interaction.response.send_message("Nisam u voice kanalu tipane.")


@bot.tree.command(name="red", description="Prikaži trenutni red čekanja.")
async def show_queue(interaction: Interaction) -> None:
    if music_player.queue.is_empty():
        await interaction.response.send_message("Red je trenutno prazan.")
    else:
        await interaction.response.send_message(embed=show_queue_embed(song_queue=music_player.queue.get_queue()))


@bot.tree.command(name="čisti", description="Očisti red čekanja.")
async def clear_queue(interaction: Interaction) -> None:
    music_player.queue.clear()
    await interaction.response.send_message("Red je očišćen.")


@bot.tree.command(name="pjevaj", description="Natjeraj me da pjevam ili dodam pjesmu u red čekanja.")
async def play_audio(interaction: Interaction, query: str) -> None:
    await interaction.response.defer()

    voice_state: VoiceState = interaction.user.voice

    if voice_state is not None:
        if not is_url(query):
            search_results = Search(query).videos
            if search_results:
                query = search_results[0].watch_url
            else:
                await interaction.response.send_message("Nisam uspjela pronaći tu pjesmu.")
                return

        song: Song = await download_song(query)

        music_player.queue.add_song(song)

        if music_player.voice_client is None:
            voice_channel: VoiceChannel = voice_state.channel
            music_player.voice_client = await voice_channel.connect()

            while not music_player.queue.is_empty():
                song: Song = music_player.queue.get_next_song()

                await music_player.play(song=song, interaction=interaction)

            await music_player.voice_client.disconnect()
            music_player.voice_client = None
            await interaction.followup.send("Uh, napjevala sam se za sada, bok!")
        else:
            await interaction.followup.send(embed=added_to_queue_embed(song=song, interaction=interaction,
                                                                       queue_length=music_player.queue.length()))
    else:
        await interaction.response.send_message(f"{interaction.user.display_name} je majmun i nije u voice kanalu.")


@play_audio.autocomplete("query")
async def play_audio_autocompletion(interaction: Interaction, current: str) -> List[Choice[str]]:
    return search(current)


def main() -> None:
    bot.run(token=DISCORD_TOKEN)


if __name__ == "__main__":
    main()
