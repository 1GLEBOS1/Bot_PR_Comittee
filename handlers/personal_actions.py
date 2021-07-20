from aiogram import types
from dispatcher import dp


@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await message.reply(text=message.from_user.id)
