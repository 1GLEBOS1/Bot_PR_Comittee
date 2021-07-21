import peewee
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from dispatcher import dp, bot
from finete_state_machine import AddMember, ViewStatistic, AddStatistic
from database.interface import InterfaceStatistic, InterfacePRCommitteeMember


# /start
@dp.message_handler(commands=['start'])
async def start(message=types.Message):
    await message.answer(text=f'Ваш telegram id: {message.from_user.id}')


# /help
@dp.message_handler(commands=['help'])
async def help_(message=types.Message):
    await message.answer(text='Заглушка')


@dp.message_handler(commands=['debug'], state='*')
async def cancel(message=types.Message, state=FSMContext):
    current_state = await state.get_state()
    await message.answer(text='Машина состояний сброшена, наши программисты уже работают над исправлением ошибки')
    await bot.send_message(chat_id=870069981, text=f'Username: {message.from_user.username}, chat_id: {message.chat.id}'
                                                   f', state: {current_state}')
    await state.finish()


# /created_db
@dp.message_handler(is_owner=True, commands=['create_db'])
async def createdb(message=types.Message):
    try:
        InterfaceStatistic.create_db()
        InterfacePRCommitteeMember.create_db()
        await message.answer(text='Базы данных созданы')
    except peewee.DatabaseError as e:
        await message.answer(text=f'Ошибка: {e}')


# /add_member
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


# /view_statistic
@dp.message_handler(is_chairman=True, commands=['view_statistic'])
@dp.message_handler(is_owner=True, commands=['view_statistic'])
async def view_get_event_id(message=types.Message):
    pass


@dp.message_handler(state=ViewStatistic.get_event_id)
async def view_add_statistic(message=types.Message, state=FSMContext):
    pass


# /add_statistic
@dp.message_handler(is_pr_comittee_member=True, commands=['add_statistic'])
@dp.message_handler(is_chairman=True, commands=['add_statistic'])
@dp.message_handler(is_owner=True, commands=['add_statistic'])
async def get_event_id(message=types.Message):
    pass


@dp.message_handler(state=AddStatistic.get_statistic)
async def get_statistic(message=types.Message, state=FSMContext):
    pass


@dp.message_handler(state=AddStatistic.add_statistic)
async def add_statistic_to_database(message=types.Message, state=FSMContext):
    pass
