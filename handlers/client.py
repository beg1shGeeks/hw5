import random

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import Dispatcher, types

async def start_command(message: types.Message):
    await message.answer("Hello world!")

async def quiz_command(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("NEXT", callback_data="button")
    markup.add(button)

    question = "В каком году были основаны курсы Geeks?"
    answers = [
        "2019",
        "2018",
        "2017",
        "2020",
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Раньше были курсы GeekTech потом был ренбрендинг и переименовали на Geeks",
        open_period=15,
        reply_markup=markup

    )

async def mem_command(message: types.Message):
    photos = (
        'media/img.png',
        'media/img_1.png',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_command, commands=['quiz'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(start_command, commands=['start'])
