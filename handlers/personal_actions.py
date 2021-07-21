from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from dispatcher import dp
from finete_state_machine import AddMember, ViewStatistic


@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await message.reply(text=f'Ваш telegram id: {message.from_user.id}', reply=False)


@dp.message_handler(is_owner=True, commands=['help'])
@dp.message_handler(is_chairman=True, commands=['help'])
async def help_(message=types.Message):
    await message.reply(text='', reply=False)


@dp.message_handler(is_owner=True, commands=['create_db'])
async def createdb(message=types.Message):
    pass


@dp.message_handler(is_owner=True, commands=['add_member'])
@dp.message_handler(is_chairman=True, commands=['add_member'])
async def get_telegram_id(message=types.Message):
    pass


@dp.message_handler(state=AddMember.get_telegram_id)
async def get_name(message=types.Message, state=FSMContext):
    pass


@dp.message_handler(state=AddMember.get_name)
async def get_access_level(message=types.Message, state=FSMContext):
    pass


@dp.message_handler(state=AddMember.get_access_level)
async def get_position(message=types.Message, state=FSMContext):
    pass


@dp.message_handler(state=AddMember.get_position)
async def add_member(message=types.Message, state=FSMContext):
    pass


#
@dp.message_handler(is_chairman=True, commands=['view_statistic'])
@dp.message_handler(is_owner=True, commands=['view_statistic'])
async def view_get_event_id(message=types.Message):
    pass


@dp.message_handler(state=ViewStatistic.get_event_id)
async def view_statistic(message=types.Message, state=FSMContext):
    pass
