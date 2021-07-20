from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter, IsOwnerOrChairmanFilter

# Inits
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

#
dp.filters_factory.resolve(IsOwnerFilter, event_handler=[dp.message_handler])
dp.filters_factory.resolve(IsChairmanFilter, event_handler=[dp.message_handler])
dp.filters_factory.resolve(IsPRComitteeMemberFilter, event_handler=[dp.message_handler])
dp.filters_factory.resolve(IsOwnerOrChairmanFilter, event_handler=[dp.message_handler])
