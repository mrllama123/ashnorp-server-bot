import logging
import os

import bot.bot as bot
# logging setup
logging.basicConfig(level=logging.INFO)
token = os.getenv("TOKEN")

if __name__ == '__main__':
    bot.start_bot(token)