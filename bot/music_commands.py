import logging
import os 
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
from bot.constants import *
from bot.ytdl_source import YTDLSource

log = logging.getLogger()
dirname = os.path.dirname(__file__)

class Music(commands.Cog):
    """
    class to hold all music commands 
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def wop(self, ctx):
        voice_clients = ctx.box.voice_clients
        for voice_client in voice_clients:
            await self.play_audio_local(voice_client, "clearly.ogg")

    @commands.command()
    async def stonks(self, ctx):
        voice_clients = ctx.bot.voice_clients
        for voice_client in voice_clients:
            await self.play_audio_local(voice_client, "stonks.mp3")
    
    @commands.command()
    async def goosebumps(self, ctx, *args):
        voice_clients = ctx.bot.voice_clients
        if any(arg in ["woof", "dog"] for arg in args):
            for voice_client in voice_clients:
                await self.play_audio_local(voice_client, "Goosebumps woof.mp3", 0.4)
        else:
            for voice_client in voice_clients:
                await self.play_audio_local(voice_client, "Goosebumps Theme Song.mp3", 0.4)
    

    @commands.command()
    async def stream(self, ctx, *, url):
        """
        streams a youtube clip (or anything else that youtube dl can play)
        :param ctx: context object
        :param url: the url for the clip
        """
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player)
        await ctx.send('Now playing: {}'.format(player.title))

    async def play_audio_local(self, voice_client, sound_file, volume=0.5):
        """
        plays audio in voice channel
        :param voice_client: voice client object
        :param sound_file: the filename of the sound file
        """
        if not voice_client.is_playing():
            sound_filename = os.path.join(dirname, "sounds", sound_file)
            sound_source = PCMVolumeTransformer(FFmpegPCMAudio(sound_filename, **ffmpeg_options), volume=volume)        
            voice_client.play(sound_source)