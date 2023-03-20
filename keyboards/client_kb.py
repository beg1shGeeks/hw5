from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('да'),
    KeyboardButton('нет')
)

cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(


    resize_keyboard=True,
    one_time_keyboard=True,
).add(

)
