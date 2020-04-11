import logging
import os 
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import youtube_dl
from bot.constants import *
from bot.music_commands import Music

log = logging.getLogger()
dirname = os.path.dirname(__file__)
env = os.getenv("ENV")
bot = commands.Bot(command_prefix='/')




def start_bot(token):
    if env == "test":
        bot.command_prefix = "/test-"
    bot.add_cog(Music(bot))
    bot.run(token)

@bot.event
async def on_ready():
    log.info("bot ready")
    guilds = bot.guilds
    for guild in guilds:
        channels = guild.channels
        voice_genral_channel = [channel for channel in channels if channel.name == "General" ][0]
        await voice_genral_channel.connect()




# @bot.command()
# async def wop(ctx):
#     bot = ctx.bot
#     voice_clients = bot.voice_clients
#     for voice_client in voice_clients:
#         await play_audio(voice_client, "clearly.ogg")

# @bot.command()
# async def stonks(ctx):
#     bot = ctx.bot
#     voice_clients = bot.voice_clients
#     for voice_client in voice_clients:
#         await play_audio(voice_client, "stonks.mp3")


# @bot.command()
# async def goosebumps(ctx, *args):
#     bot = ctx.bot
#     voice_clients = bot.voice_clients
#     if any(arg in ["woof", "dog"] for arg in args):
#         for voice_client in voice_clients:
#             await play_audio(voice_client, "Goosebumps woof.mp3", 0.4)
#     else:
#         for voice_client in voice_clients:
#             await play_audio(voice_client, "Goosebumps Theme Song.mp3", 0.4)

# async def play_audio(voice_client, sound_file, volume=0.5):
#     """
#     plays audio in voice channel
#     :param voice_client: voice client object
#     :param sound_file: the filename of the sound file
#     """
#     if not voice_client.is_playing():
#         sound_filename = os.path.join(dirname, "sounds", sound_file)
#         sound_source = PCMVolumeTransformer(FFmpegPCMAudio(sound_filename, **ffmpeg_options), volume=volume)        
#         voice_client.play(sound_source)
