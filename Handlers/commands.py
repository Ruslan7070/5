from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from config import bot, dp
from asyncio import sleep



async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Hello User {message.from_user.full_name}")


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Дальше", callback_data="next_button_1")
    markup.add(button)
    quiestion = "Кто был первым в мире программистом?"
    answers = [
        "Ilon Mask",
        "Gagarin",
        "Ada Lavleis",
        "Adham Soliev",
        "Mark Cuckerberg",
    ]
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Я думал ты умный!",
        open_period=10,
        reply_markup=markup
    )



async def send_mem(message: types.Message):
    await bot.send_photo(message.chat.id, photo=open('img/img.jpg', 'rb'))

async def dice(message: types.Message):
    await message.answer(f'{message.from_user.first_name} VS Bot')
    await sleep(2)
    await message.answer('Кость Бота')
    bot_data = await message.answer_dice()
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer(f'Кость {message.from_user.first_name}')
    user_data = await message.answer_dice()
    user_data = user_data['dice']['value']
    await sleep(5)
    if bot_data > user_data:
        await message.answer("Bot Выиграл!!!")
    elif bot_data < user_data:
        await message.answer(f'{message.from_user.first_name} Выиграл!!!')
    else:
        await message.answer('Ничья!!!')

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_mem, commands=['mem'])
    dp.register_message_handler(dice, commands=['dice'])
