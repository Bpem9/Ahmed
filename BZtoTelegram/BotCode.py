
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from BZparsing import get_content, checking_for_new_apts
from config import URL, HEADERS, ID_REG, HOUSE_TYPE_REG, HOST, tg_bot_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def hello (message: types.Message):
    await message.reply('Здорова! Напиши чета, я чекну сайт, братан')

def test():
# --- just testing mechanics, not usable function---
    html = get_content(URL)
    result = checking_for_new_apts(html)
    if isinstance(result, dict):
        for el, x in result.items():
            print(f'{el}:{x}')
    else:
        print(result)


@dp.message_handler()
async def home (message: types.Message):
    html = get_content(URL)
    result = checking_for_new_apts(html)
    if not result:
        await message.reply('Пока ничего нового, братан!')
    else:
        for el, x in result.items():
            type_of_house = x['Тип']
            house_location = x['Локация']
            price_of_house = x['Цена']
            link = x['Ссылка']
            await message.reply(f'Смотри, чё нового выложили:\n\nТип - {type_of_house},\nЛокация - {house_location},\nЦена - {price_of_house}\U000020AC,\nСсылка - {link}')


if __name__ == '__main__':
#    test()
    executor.start_polling(dp)