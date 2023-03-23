from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")

share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(
    start_button,
    help_button,
    quiz_button,
    share_location,
    share_contact
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ОТМЕНА"),
)

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("IOS"),
    KeyboardButton("ANDROID"),
    KeyboardButton("BACKEND"),
    KeyboardButton("FRONTEND"),
    KeyboardButton("UX/UI"),
    KeyboardButton("ОТМЕНА"),


)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    KeyboardButton("ОТМЕНА"),
)