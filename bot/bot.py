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
