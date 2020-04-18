import logging
import os 
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer, VoiceChannel
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
        await self.play_audio_local(ctx.voice_client, "clearly.ogg")

    @commands.command()
    async def stonks(self, ctx):
        await self.play_audio_local(ctx.voice_client, "stonks.mp3")
    
    @commands.command()
    async def goosebumps(self, ctx, *args):
        if any(arg in ["woof", "dog"] for arg in args):
            await self.play_audio_local(ctx.voice_client, "Goosebumps woof.mp3", 0.4)
        else:
            await self.play_audio_local(ctx.voice_client, "Goosebumps Theme Song.mp3", 0.4)
    
    @commands.command()
    async def join(self, ctx, *, channel: VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command()
    async def disconect(self, ctx):
        """Stops and disconnects the bot from voice"""
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        await ctx.voice_client.disconnect()

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")
        if not ctx.voice_client.source is None:
            ctx.voice_client.source.volume = volume / 100
            await ctx.send("Changed volume to {}%".format(volume))
        else:
            await ctx.send("Not connected to a voice channel.")



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

    @stream.before_invoke
    @wop.before_invoke
    @stonks.before_invoke
    @goosebumps.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()