from aiogram import Dispatcher, types


async def mem(message: types.message):
    with open('images/img.jpg', 'rb') as img:
        await message.answer_photo(photo=img)


async def pin_handler(message: types.Message):
    if message.reply_to_message:
        message_to_pin = message.reply_to_message
        await message_to_pin.pin()
        await message.answer("Сообщение закреплено!")
    else:
        await message.answer("Воспользуйся этой командой что бы закрепить сообщение.")


def register_hadlers_extra(dp: Dispatcher):
    dp.register_message_handler(pin_handler, commands=['pin'],commands_prefix='!/')
    dp.register_message_handler(mem, commands=['mem'])