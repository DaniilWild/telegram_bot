import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text
from random import randint
from aiogram.types import Sticker
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.utils.emoji import emojize
import asyncio

#from flask import Flask, request
import requests

def skl(x) :
    f1 = lambda a: (a%100)//10 != 1 and a%10 == 1
    f2 = lambda a: (a%100)//10 != 1 and a%10 in [2,3,4]
    return " градус" if f1(x) else  " градуса" if f2(x) else " градусов"


def get_weather():
    params = {"access_key": "03f637409974d3bd297d1d269e4a87f8", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    grad = api_response['current']['temperature']
    send  = "Сейчас в Москве " + str(grad) + skl(abs(grad))
    return send

# Объект бота
bot = Bot(token="1760292725:AAEp-FM34YAt8zMM59pnv73NeWvZm2kwAuE")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Привет Бот", "Что ты умеешь?", "Помоги с выбором одежды" , "Какая cейчас погода?"]
    keyboard.add(*buttons)
    await message.answer("Возможности бота", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Привет Бот")
async def hello(message: types.Message):
    await message.answer(emojize("Привет Аня!"))
    await message.answer(emojize(":wave:"))


@dp.message_handler(lambda message: message.text == "Какая cейчас погода?")
async def weather(message: types.Message):
    await message.answer(get_weather())

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
    click = randint(0,2)
    if click == 0:
        await message.answer("Оно сидит на тебе <b>идеально</b> !" , parse_mode=types.ParseMode.HTML)
    else:
        await message.answer("Вообше не идет" , parse_mode=types.ParseMode.HTML)

#await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())



# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

executor.start_polling(dp, skip_updates=True)


