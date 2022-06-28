
import requests
from config import open_api_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from WeatherParsing import get_weather

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def message (message: types.Message):
    await message.reply('Привет! Для получения погоды, напиши город')

@dp.message_handler()
async def weather (message: types.Message):
    await message.reply(get_weather(message['text'], open_api_token))

if __name__ == '__main__':
    executor.start_polling(dp)
