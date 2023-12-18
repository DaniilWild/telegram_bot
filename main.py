import asyncio
import requests
import logging

from aiogram import Bot, Dispatcher, executor, types
from random import randint
from aiogram.types import Sticker
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.utils.emoji import emojize
from apscheduler.schedulers.blocking import BlockingScheduler

# Кастомный модуль
from weather_requests import get_weather, skl


# Объект бота
bot = Bot(token="1760292725:AAEp-FM34YAt8zMM59pnv73NeWvZm2kwAuE")
# Диспетчер для бота
dp = Dispatcher(bot)
# Планровшик времени
sched = BlockingScheduler()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Привет Бот", "Что ты умеешь?", "Помоги с выбором одежды" , "Погода", "Расскажи шутку" , "Гороскоп"]
    keyboard.add(*buttons)
    await message.answer("Возможности бота", reply_markup=keyboard)

# Бот здоровается
@dp.message_handler(lambda message: message.text == "Привет Бот")
async def hello(message: types.Message):
    await message.answer(emojize("Привет Аня!"))
    await message.answer(emojize(":wave:"))

# Работа с Api погоды
@dp.message_handler(lambda message: message.text == "Погода")
async def weather(message: types.Message):
    await message.answer(get_weather()[0])
    await message.answer(emojize(get_weather()[1] + " :umbrella:"))
    #await bot.send_photo(message.chat.id, requests.get(get_weather()[1]).content , caption="Holidays!")

@dp.message_handler(lambda message: message.text == "Расскажи шутку")
async def joke(message: types.Message):
    api_result = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
    api_response = api_result.json()
    await message.answer(api_response["joke"])

@dp.message_handler(lambda message: message.text == "Гороскоп")
async def star(message: types.Message):
    api_result = requests.get('http://horoscope-api.herokuapp.com/horoscope/today/Gemini')
    api_response = api_result.json()
    await message.answer(api_response['horoscope'])

@dp.message_handler(lambda message: message.text == "Что ты умеешь?")
async def help(message: types.Message):
    await message.answer("  1) <b>'Привет Бот'</b> - поздороваться с ботом \n 2) <b>'Помоги с выбором одежды'</b> - на случай если нужен совет брать или не брать вешь\n 3) <b> 'Какая cейчас погода?' </b> - Погода в Москве на час\n 4) <b> 'Расскажи шутку' </b> - случайная батина сальная шутка на английском\n 5) <b> 'Гороскоп'</b> - гороскоп на сегодня с сУрьезного западного сайта", parse_mode=types.ParseMode.HTML)

@dp.message_handler(lambda message: message.text == "Помоги с выбором одежды")
async def random_swit(message: types.Message):
    await message.answer("Хмммм дай подумать")
    await asyncio.sleep(0.5)

    click = randint(0,5)
    if click == 0:
        await message.answer_sticker(r'CAACAgIAAxkBAAEBBI9gV7gSuahfGjTGq86uvelzvNdsgAACGAADwDZPE9b6J7-cahj4HgQ')
    elif click == 1:
        await message.answer_sticker(r'CAACAgIAAxkBAAEBBJJgV7iExyEC8LCf1At8gZxf7Gf1DwACOwMAAm2wQgMDgo__5XFPdR4E')
    elif click == 2:
        await message.answer_sticker(r'CAACAgUAAxkBAAEBBJVgV7iVAdJZcKVNRAIDYEjVEkkolAAC4QYAAszG4gLDJmXp-6nvCR4E')
    elif click == 3:
        await message.answer_sticker(r'CAACAgIAAxkBAAEBBJhgV7n1qKndabTiJBYPZPaR69V40QACGwADrWW8FOEKYLlsBxzjHgQ')
    elif click == 4:
        await message.answer_sticker(r'CAACAgIAAxkBAAEBBJtgV7okHwGD9v1CEqSmSZCixRMX6gAC7wEAAladvQrc_Ul1tTRfQB4E')
    else:
        await message.answer_sticker(r'CAACAgIAAxkBAAEBBI9gV7gSuahfGjTGq86uvelzvNdsgAACGAADwDZPE9b6J7-cahj4HgQ')

    await asyncio.sleep(1)
    click = randint(0,11)
    if click == 0:
        await message.answer("Оно сидит на тебе <b>идеально</b> !" , parse_mode=types.ParseMode.HTML)
    elif click == 1:
        await message.answer("Забей и накупи вкусняшек на эти деньги")
    elif click == 2:
        await message.answer("Выглядит классно, но я бы подождал скидок!")
    elif click == 3:
        await message.answer("Если тебе нужен знак, то вот он!")
    elif click == 4:
        await message.answer("Купишь со стипедии")
    elif click == 5:
        await message.answer("Оно того не стоит")
    elif click == 6:
        await message.answer("Я бы хотел это прмерить но я всего лишь бот( ")
    elif click == 7:
        await message.answer("Тебе к лицу")
    elif click == 8:
        await message.answer("Тебе не к лицу")
    elif click == 9:
        await message.answer("Это не черный худи но пойдет")
    else:
        await message.answer("Вообше не идет" , parse_mode=types.ParseMode.HTML)

if __name__ == '__main__':
    #Хэндлер на команду работу в 9 утра беззвука
    @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17, minute=41 )
    
    sched.configure(options_from_ini_file)
    executor.start_polling(dp, skip_updates=True)
    sched.start()
