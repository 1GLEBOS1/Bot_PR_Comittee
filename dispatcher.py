from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter, IsOwnerOrChairmanFilter

# Inits
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

#
dp.filters_factory.resolve(IsOwnerFilter, dp.message_handler())
dp.filters_factory.resolve(IsChairmanFilter, dp.message_handler())
dp.filters_factory.resolve(IsPRComitteeMemberFilter, dp.message_handler())
dp.filters_factory.resolve(IsOwnerOrChairmanFilter, dp.message_handler())
