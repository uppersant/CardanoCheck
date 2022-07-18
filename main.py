from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import json

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
	await bot.send_message(msg.from_user.id, "👋 Привет!", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🔄 Обновить прогресс')))


@dp.message_handler()
async def text(msg: types.Message):
	if msg.text.lower() == "🔄 обновить прогресс":
		await bot.send_message(msg.from_user.id, f'Прогресс: {json.loads(requests.get("http://localhost:8090/v2/network/information/").text)["sync_progress"]["progress"]["quantity"]}%')


if __name__ == '__main__':
	executor.start_polling(dp)
