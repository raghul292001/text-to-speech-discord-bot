# from discord.ext import commands
# from utils.tts import text_to_speech
# import discord
# import os

# class TTSCommand(commands.Cog):
#     """
#     A command cog for generating text-to-speech from given text.
#     """
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(name="speak", help="Convert the given text to speech and send it as an MP3.")
#     async def speak(self, ctx, *, text: str):
#         try:
#             # Convert the provided text to speech
#             await ctx.send("Converting text to speech...")

#             # Call the function to convert text to speech
#             audio_file = text_to_speech(text)

#             # Send the audio file as an attachment in the same channel
#             await ctx.send("Here is the audio:", file=discord.File(audio_file))

#             # Clean up the temporary audio file after sending
#             os.remove(audio_file)

#         except Exception as e:
#             await ctx.send(f"An error occurred: {str(e)}")

from discord.ext import commands
from utils.tts import text_to_speech
import discord
import os

class TTSCommand(commands.Cog):
    """
    A command cog for generating text-to-speech.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="speak", help="Convert provided text to speech and send the MP3 file.")
    async def speak(self, ctx, *, prompt: str):
        try:
            # Convert text to speech and get the audio file path
            audio_file = text_to_speech(prompt)

            # Send the MP3 file to the channel
            await ctx.send("Here is your text-to-speech response:", file=discord.File(audio_file))

            # Optionally, remove the file after sending
            os.remove(audio_file)

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
