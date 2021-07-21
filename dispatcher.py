from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter

# Inits
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Activation filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsChairmanFilter)
dp.filters_factory.bind(IsPRComitteeMemberFilter)
