import sys
from pyrogram import Client
from telethon.sync import TelegramClient
import uvloop
from config import API_ID, API_HASH, BOT_TOKEN

# Adjusting the first bot's parameters
bot = TelegramClient('premiumrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Pyrogram Client optimized for 1k users
Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH,
    workers=50,  # Increase workers to handle more concurrent requests
    sleep_threshold=10,  # Adjusting the threshold to handle rate limits
    max_concurrent_transmissions=50  # Increased to manage more concurrent file/message transmissions
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)

# Optimized second bot
modi = Client(
    "modibot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH,
    workers=50,
    sleep_threshold=10,
    max_concurrent_transmissions=50
)    

try:
    modi.start()
except Exception as e:
    sys.exit(1)

# Optimized third bot
sigma = Client(
    "sigma",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH,
    workers=50,
    sleep_threshold=10,
    max_concurrent_transmissions=50
)    

try:
    sigma.start()
except Exception as e:
    sys.exit(1)

# Adjusting the fourth bot's parameters
sex = TelegramClient('sexrepo', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
