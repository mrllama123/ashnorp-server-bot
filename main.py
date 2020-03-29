import logging
import os
import discord
import bot.bot_actions as bot
# logging setup
logging.basicConfig(level=logging.INFO)
token = os.getenv("TOKEN")

if __name__ == '__main__':
    bot.start_bot(token)