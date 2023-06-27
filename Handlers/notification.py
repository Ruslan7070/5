import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from database.bot_db import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger

async def get_up():
    users = await sql_command_all_ids()
    for user in users:
        await bot.send_message(
            user [0], "ПОРА ВСТАВАТЬ!"

        )



async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        get_up,
        CronTrigger(
        year=2023,month=6,day=27,hour=19,minute=0
        )

    )


    scheduler.start()