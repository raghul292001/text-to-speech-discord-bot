# text to speech discord bot

Text-to-Speech Discord Bot 🎤🤖
This repository contains a Discord bot designed to convert user-input text into speech using Python. The bot leverages pyttsx3 for text-to-speech synthesis, enabling support for natural-sounding male voices (e.g., Microsoft voices on Windows). It allows users to generate speech and play it directly in a Discord voice channel.

Features 🚀
Text-to-Speech Conversion: Converts any text input into high-quality speech.
Custom Voices: Configured to use natural-sounding male voices for better user experience.
Voice Channel Integration: Plays the generated audio directly in a user's current voice channel.
Free and Open-Source: Uses entirely free tools and libraries (pyttsx3), ensuring no additional costs.

Project Structure 📂

project/
├── bot.py # Main entry point of the bot
├── command/
│ ├── **init**.py # Package initializer for commands
│ ├── tts_command.py # Cog for the text-to-speech command
├── utils/
│ ├── **init**.py # Package initializer for utilities
│ ├── tts.py # Text-to-speech logic with pyttsx3
├── config/
│ └── config.py # Configuration for API keys and bot settings
├── requirements.txt # Python dependencies
Setup Instructions ⚙️
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/tts-discord-bot.git
cd tts-discord-bot
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your bot:

Open config/config.py and update DISCORD_TOKEN with your Discord bot token.
Ensure you have the correct FFMPEG_PATH set if required.
Run the bot:

bash
Copy code
python bot.py
Prerequisites ✅
Python 3.8+: Ensure Python is installed.
FFmpeg: Required for playing audio in Discord. Download here.
Discord Bot Token: Register your bot on the Discord Developer Portal.
Contributing 🤝
Contributions are welcome! Feel free to fork the repository and submit pull requests.

License 📜
This project is licensed under the MIT License.
