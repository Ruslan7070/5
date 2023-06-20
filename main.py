from aiogram import executor
import logging

import fsm_mentor
from config import dp
from Handlers import commands, callback, extra, admin


Commands.register_handlers_commands(dp)
Callback.register_handlers_callback(dp)
Admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_anketa(dp)
Extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
