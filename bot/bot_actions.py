import discord
import logging
import os 
from random import randint

log = logging.getLogger()
client = discord.Client()

voice_client_genral = None

def start_bot(token):
    """
    starts the bot client
    """
    client.run(token)

@client.event
async def on_ready():
    """
    runs once client is connected to discord
    """
    log.info("sucessfully connected to discord as " + client.user.name)

@client.event
async def on_message(message):
    """
    main fucntion that gets ran everytime a message is sent to bot
    """
    if message.content.lower().startswith("/roll"):
        value = dice_action(message)
        if value is None:
            await message.channel.send("error with command `" + message.content + "` use `/roll <d4, d6, d8, d10, d12, d20>`")
        else:
            await message.channel.send(str(value))
    elif message.content.lower().startswith("/wop"):
        await wop_action(message)
    elif  message.content.lower().startswith("/join voice"):
        await join_genral_voice_chat(message)  
    elif  message.content.lower().startswith("/diconnect voice"):
        await disconnect_genral_voice_chat(message)  


async def join_genral_voice_chat(message):
    """
    joins genral discord channel
    :param message: message
    """
    global voice_client_genral
    if voice_client_genral is None:
        channels = message.guild.channels
        voice_genral_channel = [channel for channel in channels if channel.name == "General" ][0]
        voice_client_genral = await voice_genral_channel.connect()


async def disconnect_genral_voice_chat(message):
    """
    disconnect genral discord channel
    :param message: message
    """
    global voice_client_genral
    channels = message.guild.channels
    voice_genral_channel = [channel for channel in channels if channel.name == "General" ][0]
    if voice_client_genral is not None:
        await voice_client_genral.disconnect()
        voice_client_genral = None

async def wop_action(message):
    """
    joins a voice channel and play sound effect
    :param message: the message object
    """
    if voice_client_genral is not None and not voice_client_genral.is_playing():
        log.info("playing wop sound ?")
        dirname = os.path.dirname(__file__)
        sound_filename = os.path.join(dirname, "sounds/clearly.ogg") 
        voice_client_genral.play(discord.FFmpegPCMAudio(sound_filename)) 
        while voice_client_genral.is_playing():
            pass

    # get a list of all channels in server
    # channels = message.guild.channels
    # get General voice chat
    # voice_genral_channel = [channel for channel in channels if channel.name == "General" ][0]
    # voice_channel =  await voice_genral_channel.connect()
    # dirname = os.path.dirname(__file__)
    # sound_filename = os.path.join(dirname, "sounds/clearly.ogg") 



def dice_action(message):
    """
    do dice actions
    :param message: the dicord message object 
    :return: return dice number if valid dice command or none
    """
    if "d20" in message.content.lower():
        return randint(1,20)
    elif "d12" in message.content.lower():
        return randint(1,11)
    elif "d10" in message.content.lower():
        return randint(1,9)
    elif "d8" in message.content.lower():
        return randint(1,8)
    elif "d6" in message.content.lower():
        return randint(1,6)
    elif "d4" in message.content.lower():
        return randint(1,4)
    else:
        return None


