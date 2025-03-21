# Discord Music Bot

This is a simple Discord music bot that can play music from YouTube, manage a song queue, and handle various
music-related
commands.

## Features

- Play music from YouTube
- Manage a song queue
- Pause, resume, and skip songs
- Display the current queue
- Clear the queue
- Automatically disconnect when not in use

## Commands

- `/pjevaj <pjesma>`: Play a song or add it to the queue.
- `/red`: Display the current queue.
- `/čisti`: Clear the queue.
- `/bok`: Disconnect the bot from the voice channel.
- `/pauziraj`: Pause the current song.
- `/nastavi`: Resume the paused song.
- `/preskoči`: Skip the current song.
- `/upomoć`: List all available commands.

## prerequisites

- Have Docker installed
- Have a Discord bot with `Message Content Intent` enabled, which you can do [here](https://discord.com/developers/applications) under the `Bot` setting

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/lukaznj/discord-music-bot.git
    cd discord-music-bot
    ```

2. Rename the `.env.example` file into `.env` and fill in your Discord token
    ```dotenv
    DISCORD_TOKEN=<your-discord-token>
    ```

3. Create a Docker image:
    ```bash
    docker build -t lukaznj/discord-music-bot:1.0 .
    ```

4. Run the Docker image:
   ```bash
   docker run --env-file .env lukaznj/discord-music-bot:1.0
   ```

## License

This project is licensed under the MIT License.
