import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import asyncio

api_id = '19682435'
api_hash = '6df07025a063974949716694bcf205ca'
token = '5169620726:AAG7vhr2mwm-z7qgG59zFyLs90mSj39Aqvs'
phone = '+79957808190'
bot_token = '5169620726:AAG7vhr2mwm-z7qgG59zFyLs90mSj39Aqvs'
client = TelegramClient('session', api_id, api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# client.connect()

async def send_message(message):
    try:
        await bot.send_message('dva_poltora', message)
        await bot.send_message(1083151092, message)
    except Exception as e:
        print(e);

    # client.disconnect()

def send_async_telegram_message(message):
    with bot:
        client.loop.run_until_complete(send_message(message))
