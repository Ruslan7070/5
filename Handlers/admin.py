from aiogram import types, Dispatcher
from config import bot, ADMINs

async def pin_message(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("Вы не являетесь администратором")
    elif not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение")
    elif message.text.startswith('game'):
        await message.answer_dice('⚽️,🏀,🎲,🎯,🎰,🎳')
    else:
        await message.pin()







def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!/')
