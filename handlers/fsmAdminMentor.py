from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import KURATOR
from data_base.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    id_mentors = State()
    direction = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in KURATOR and message.text.startswith('/reg'):
        if message.chat.type == "private":
            await FSMAdmin.name.set()
            await message.answer("Как тебя звать?",reply_markup=client_kb.cancel_markup)
        else:
             await message.answer("Пиши в личке!")
    elif not message.from_user.id in KURATOR and message.text.startswith('/reg'):
        await message.answer("Вы не являетесь администратором (КУРАТОРОМ)")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = message.from_user.username
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?",reply_markup=client_kb.cancel_markup)

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif int(message.text) < 12 or int(message.text) > 40:
        await message.answer("Возрастное ограничение!")
    else:
        async with state.proxy() as data:
            data ['age'] = message.text
        await FSMAdmin.next()
        await message.answer("укажите id:",reply_markup=client_kb.cancel_markup)

async def load_id(message: types.Message, state: FSMContext):
     if not message.text.isdigit():
        await message.answer('Пиши числа!')
     elif int(len(message.text))<=9:
         await  message.answer("Вы ввели число, которое состоит не более чем из 10 цифр")
     else:
         async with state.proxy() as data:
             data ['id_mentors'] = message.text
         await FSMAdmin.next()
         await message.answer("какое у тебя направление?",reply_markup=client_kb.direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in \
            ["IOS", "ANDROID",  "BACKEND", "FRONTEND", "UX/UI", "Основы программирование","ОТМЕНА"]:
        await message.answer('неправильный вариант')
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer("с какой группы?",reply_markup=client_kb.cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
   if message.text.isalpha():
       await message.answer("Пиши числа!")
   else:
        async with state.proxy() as data:
            data['group'] = message.text
            await message.answer(f"имя:{data['name']}\n"
                                 f"возраст:{data['age']}\n"
                                 f"id:{data['id_mentors']}\n"
                                 f"направление:{data['direction']}\n"
                                 f"и группа:{data['group']}")
        await FSMAdmin.next()
        await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган!")
    elif message.text == "ЗАНОВО":
        await FSMAdmin.name.set()
        await message.answer("Как звать?",
                             reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("НИПОНЯЛ!?")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_id, state=FSMAdmin.id_mentors)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)