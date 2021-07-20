from aiogram import executor
from dispatcher import dp
import logging

logging.basicConfig(level=logging.INFO)

if True:
    executor.start_polling(dp, skip_updates=True)
