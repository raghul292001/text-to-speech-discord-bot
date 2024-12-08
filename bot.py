# import discord
# from discord.ext import commands
# from commands.tts_command import TTSCommand
# from config.config import DISCORD_TOKEN, COMMAND_PREFIX

# # Enable specific intents
# intents = discord.Intents.default()
# intents.messages = True          # For reading messages
# intents.message_content = True   # For message content processing (required for command recognition)
# intents.guilds = True            # For guild-related events


# # Create bot instance
# bot = commands.Bot(command_prefix="!", intents=intents)

# # Load command cogs
# bot.add_cog(TTSCommand(bot))


# @bot.event
# async def on_ready():
#     print(f"Bot connected as {bot.user}")

# # Run the bot
# if __name__ == "__main__":
#     bot.run(DISCORD_TOKEN)


import discord
from discord.ext import commands
from commands.tts_command import TTSCommand
from config.config import DISCORD_TOKEN, COMMAND_PREFIX
import asyncio


# Enable specific intents
intents = discord.Intents.default()
intents.messages = True          # For reading messages
intents.message_content = True   # For message content processing (required for command recognition)
intents.guilds = True            # For guild-related events

# Create bot instance
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Load command cogs asynchronously
@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.add_cog(TTSCommand(bot))  # Await add_cog()

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
