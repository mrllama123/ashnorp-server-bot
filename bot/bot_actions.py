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
    if "d20" in message.content.lower():
        value = randint(1,20)
        await message.channel.send(str(value))
    elif "d12" in message.content.lower():
        value = randint(1,11)
        await message.channel.send(str(value))
    elif "d10" in message.content.lower():
        value = randint(1,9)
        await message.channel.send(str(value))