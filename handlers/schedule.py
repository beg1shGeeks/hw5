import datetime
from aiogram import Bot
from data_base.bot_db import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.cron import CronTrigger
# from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot


async def go_to_eat_for_iftar(bot:Bot):

    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0],f'Время для ифтара {user[1]}')



async def set_schedler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        go_to_eat_for_iftar,
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2023,month=3,day=24,hour=22,minute=20,second=0
            )
        ),
        kwargs={'bot':bot}
    )
    scheduler.start()