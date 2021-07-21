from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter

# Inits
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Activation filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsChairmanFilter)
dp.filters_factory.bind(IsPRComitteeMemberFilter)
