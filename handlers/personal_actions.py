from aiogram import types
from dispatcher import dp
from filter import IsOwnerFilter, IsChairmanFilter, IsPRComitteeMemberFilter


@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await message.reply(text=f'Ваш telegram id: {message.from_user.id}', reply=False)


@dp.message_handler(is_owner=True, commands=['help'])
@dp.message_handler(is_chairman=True, commands=['help'])
async def help_(message=types.Message):
    await message.reply(text='', reply=False)
