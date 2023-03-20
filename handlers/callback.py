from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("NEXT", callback_data="button1")
    markup.add(button)

    question = "Сколько человек в группе 27-02?"
    answers = [
        "6",
        "9",
        "5",
        "8",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="IOS, Android, PM, Backend, Frontend, UX/UI, Основы программирование, Fullstack",
        open_period=15,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT", callback_data="button2")
    markup.add(button1)

    question = "сколько менторов в geeks?"
    answers = [
        "1",
        "70",
        "75",
        "22",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать(",
        open_period=20,
        reply_markup=markup
    )


# @dp.callback_query_handler(text="button4")
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT", callback_data="button3")
    markup.add(button2)

    question = "Сколько месяцев в году?"
    answers = [
        "8м",
        "11м",
        "12м",
        "9м",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать(",
        open_period=20,
        reply_markup=markup

    )


async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT", callback_data="button4")
    markup.add(button2)

    question = "Самое лучшее направление?"
    answers = [
        "Frontend",
        "Android",
        "IOS",
        "Backend",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Backend лучший",
        open_period=20,
        reply_markup=markup

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button")
    dp.register_callback_query_handler(quiz_3, text="button1")
    dp.register_callback_query_handler(quiz_4, text="button2")
    dp.register_callback_query_handler(quiz_5, text="button3")