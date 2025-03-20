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

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your tokens:
    ```dotenv
    DISCORD_TOKEN=<your-discord-token>
    YOUTUBE_TOKEN=<your-youtube-token>
    FFMPEG_PATH=<path-to-ffmpeg>
    ```

5. Run the bot:
    ```bash
    python main.py
    ```

## Dependencies

- `discord.py`
- `pytube`
- `python-dotenv`

## License

This project is licensed under the MIT License.