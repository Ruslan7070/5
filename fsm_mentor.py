from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State,StatesGroup
from config import ADMINs
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    gender = State()
    group = State()
    submit = State()
async def fsm_start(message: types.Message,state: FSMContext):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer("Как мне тебя звать?")
    elif message.from_user.id not in ADMINs:
        await message.answer("Вы не являетесь администратором")
    else:
        await message.reply("ПИШИ В ЛИЧКУ!")


async def load_name(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("На каком направлении ты учишься?")

async def load_direction(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
        print(await state.get_state())
    await FSMAdmin.next()
    await message.answer('Сколько тебе лет?')

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("ПИШИ ЧИСЛА!")
    elif not 14 < int(message.text) < 50:
        await message.answer("Доступ запрещен,ваш возраст не соответсвует требованиям")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Ты парень или девушка?')

async def load_gender(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer("В какой группе ты учишься?")

async def load_groups(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await message.answer(f"{data['name']} {data['direction']} {data['age']} {data['gender']} {data['group']}")
    await FSMAdmin.next()
    await message.answer("Все верно?")

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Я сохранил ваши данные!")
    elif message.text.lower() == "записать снова":
        await FSMAdmin.name.set()
def register_handlers_fsm_anketa(dp:Dispatcher):
    dp.register_message_handler(fsm_start,commands=['reg'])
    dp.register_message_handler(load_name, state= FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_groups, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
