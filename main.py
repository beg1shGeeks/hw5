from aiogram.utils import executor
import logging

from config import dp,bot , ADMINS
from handlers import client, callback,  admin, extra,fsmAdminMentor,schedule
from data_base.bot_db import sql_create
async def on_startup(dp):
    await schedule.set_schedler()
    await bot.send_message(ADMINS[0], "Я родился!")
    sql_create()


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "ПОКА ПОКА!")


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_hadlers_extra(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
admin.register_handlers_client(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True,
                           on_startup=on_startup,on_shutdown=on_shutdown)