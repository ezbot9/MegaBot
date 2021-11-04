from pyrogram import Client
from config import Config

plugins = dict(root="megadl/modules")
meganzbot = Client(
        "MegaBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
