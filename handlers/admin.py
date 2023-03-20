import random
from config import ADMINS
from aiogram import Dispatcher, types


async def emoji(message: types.Message):
    if message.from_user.id in ADMINS and message.text.startswith('game'):
        emojis = ['🏀', '⚽️', '🎯', '🎳', '🎰', '🎲']
        random_emoji = random.choice(emojis)
        await message.answer_dice(random_emoji)
    elif not message.from_user.id in ADMINS and message.text.startswith('game'):
        await message.answer("Вы не являетесь админом")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(emoji)