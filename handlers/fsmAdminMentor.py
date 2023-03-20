from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import submit_markup, cancel_markup


class FSMAdmin(StatesGroup):
    ID = State()
    name = State()
    Direction = State()
    age = State()
    Group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.ID.set()
        await message.answer("Как звать?? ЭЭУУУ", reply_markup=cancel_markup)
    else:
        await message.answer("Пиши в группу!")

async def load_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ID'] = message.text
    await FSMAdmin.next()
    await message.answer('Имя ментора ?')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = message.from_user.username
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Скока лет?")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['Direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора ?')

async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['Age'] = message.text
    await FSMAdmin.next()
    await message.answer('Группа ментора ?')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['Group'] = message.text
        await message.answer(f"Информация о менторе: \n\n"
                             f"ID-ментора: {FSMCONTEXT_PROXY_STORAGE['ID']} \n"
                             f"Имя ментора: {FSMCONTEXT_PROXY_STORAGE['Name']} \n"
                             f"Направление ментора: {FSMCONTEXT_PROXY_STORAGE['Direction']} \n"
                             f"Возраст ментора: {FSMCONTEXT_PROXY_STORAGE['Age']} \n"
                             f"Группа ментора: {FSMCONTEXT_PROXY_STORAGE['Group']} \n")

    await FSMAdmin.next()
    await message.answer('Всё верно ?', reply_markup=submit_markup)

async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await message.answer('Готово!')
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Не получилось -_-')
        await state.finish()

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg_mentor'])
    dp.register_message_handler(load_ID, state=FSMAdmin.ID)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.Direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.Group)
    dp.register_message_handler(load_submit, state=FSMAdmin.submit)