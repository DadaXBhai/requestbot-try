# Developed By : Abhishek Kumar (https://telegram.me/TheTeleRoid) 

import os
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hᴇʏ! {}

Hi, I am Request Bot🤖 For DaDa Encodes.

Thank You!. For Using Me!!!.

Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

