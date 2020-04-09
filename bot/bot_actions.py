import discord
import logging
import os 
from random import randint

log = logging.getLogger()
client = discord.Client()

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


async def wop_action(message):
    """
    joins a voice channel and play sound effect
    :param message: the message object
    """
    # get a list of all channels in server
    channels = message.guild.channels
    # get General voice chat
    voice_channel = [channel for channel in channels if channel.name == "General" ][0]
    
    print("fdsklhbfdsuj")
    


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


