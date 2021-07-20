from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter, IsOwnerOrChairmanFilter

# Inits
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
