from aiogram import executor
import logging
import fsm_mentor
from config import dp,ADMINs, bot
from Handlers import commands, callback, extra, admin, notification
from database.bot_db import sql_create


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)

async def on_startup(db):
    sql_create()
    await bot.send_message(ADMINs[0], "Helloworld!")
    await notification.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(ADMINs[0], "Пока мир!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
