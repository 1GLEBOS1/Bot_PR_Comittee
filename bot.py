from aiogram import executor
from dispatcher import dp

if True:
    executor.start_polling(dp, skip_updates=True)