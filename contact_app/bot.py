import os

# Telegram, Aiogram
from aiogram import Bot

# Env
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ID = os.environ.get("ADMIN_ID")

bot = Bot(token=TOKEN)

async def send_data(data):
	try:
		await bot.send_message(ID, "NEW CONTACT MESSAGE")
		await bot.send_message(ID, data)
		await bot.send_message(ID, "🫡")
		print(ID)
	except:
		await bot.send_message(ID, "Failed to send the data")
