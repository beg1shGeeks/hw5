from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import Dispatcher, types
from data_base.bot_db import sql_command_random

async def quiz1(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("следущий вопрос?", callback_data="button_1")
    markup.add(button)

    question = "сколько дней до лета?"
    answers = [
        "20",
        "18",
        "27",
        "хз",
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="стыдно не знать!",
        open_period=15,
        reply_markup=markup

    )
async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        caption=f"{random_user[2]} {random_user[3]} {random_user[4]} "
                f"{random_user[5]}\n@{random_user[1]}"
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
