import aiogram.utils.exceptions
import peewee
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from dispatcher import dp, bot
from finete_state_machine import AddMember, ViewStatistic, AddStatistic, DeleteMember, ViewStats
from database.interface import InterfaceStatistic, InterfacePRCommitteeMember
from statistic_analyser.analyser import Analyser


# /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text=f"Ваш telegram id: {message.from_user.id}")


# /help
@dp.message_handler(commands=["help"])
async def help_(message: types.Message):
    await message.answer(text="Это бот для внутреннего использования Комитета ПИАРа Ученического совета г.Краснодар.\n"
                              "Этот бот умеет собирать статистику по пиару мероприятий.\n"
                              "Если у Вас есть вопросы, пишите их @Gleb_Polyakov")


# /debug
@dp.message_handler(commands=["debug"], state="*")
async def debug(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await message.answer(text="Машина состояний сброшена, наши программисты уже работают над исправлением ошибки")
    await bot.send_message(chat_id=-554348036, text=f"Username: {message.from_user.username}, "
                                                    f"chat_id: {message.chat.id}, "
                                                    f"state: {current_state}")
    await state.finish()


# /created_db
@dp.message_handler(is_owner=True, commands=["create_db"])
async def createdb(message: types.Message):
    try:
        InterfaceStatistic.create_db()
        InterfacePRCommitteeMember.create_db()
        await message.answer(text="Базы данных созданы")
    except peewee.DatabaseError as e:
        await message.answer(text=f"Ошибка: {e}")
        await bot.send_message(chat_id=870069981, text=f"Username: {message.from_user.username}, "
                                                       f"chat_id: {message.chat.id}"
                                                       f", error: {e}")


# /add_member
@dp.message_handler(is_owner=True, commands=["add_member"])
@dp.message_handler(is_chairman=True, commands=["add_member"])
async def get_telegram_id(message: types.Message):
    await AddMember.first()
    await message.answer(text="Введите telegram id:")


@dp.message_handler(state=AddMember.get_telegram_id)
async def get_name(message: types.Message, state: FSMContext):
    try:
        await state.update_data(telegram_id=int(message.text))
        await message.answer(text="Введите имя:")
        await AddMember.next()
    except ValueError:
        await message.answer(text="Вводите telegram id цифрами")
        await state.finish()


@dp.message_handler(state=AddMember.get_name)
async def get_access_level(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Введите уровень доступа:")
    await AddMember.next()


@dp.message_handler(state=AddMember.get_access_level)
async def get_position(message: types.Message, state: FSMContext):
    try:
        await state.update_data(access_level=int(message.text))
        await message.answer(text="Введите позицию:")
        await AddMember.next()
    except ValueError:
        await message.answer(text="Вводите уровень доступа цифрами")
        await state.finish()


@dp.message_handler(state=AddMember.get_position)
async def add_member(message: types.Message, state: FSMContext):
    await state.update_data(position=message.text)
    person_data = await state.get_data()
    try:
        InterfacePRCommitteeMember.add_member(
            telegram_id=person_data["telegram_id"],
            name=person_data["name"],
            access_level=person_data["access_level"],
            position=person_data["position"]
        )
        await message.answer(text="Успешно")
    except peewee.DatabaseError as e:
        await message.answer(f"Ошибка: {e}")
        await bot.send_message(chat_id=870069981,
                                text=f"Username: {message.from_user.username}, chat_id: {message.chat.id}"
                                    f", error: {e}"
                                )

    finally:
        await state.finish()


# /view_statistic
@dp.message_handler(is_chairman=True, commands=["view_statistic"])
@dp.message_handler(is_owner=True, commands=["view_statistic"])
async def view_get_event_id(message: types.Message):
    await message.answer(text="Введите id мероприятия")
    await ViewStatistic.first()


@dp.message_handler(state=ViewStatistic.get_event_id)
async def view_add_statistic(message: types.Message, state: FSMContext):
    try:
        await state.update_data(event_id=int(message.text))
        get_data = await state.get_data()
        a = Analyser()
        await message.answer(text=a.get_stats(event_id=get_data["event_id"]))
        del a
    except ValueError:
        await message.answer(text="Вводите id мероприятия цифрами")
    finally:
        await state.finish()


# /add_statistic
@dp.message_handler(is_pr_comittee_member=True, commands=["add_statistic"])
@dp.message_handler(is_chairman=True, commands=["add_statistic"])
@dp.message_handler(is_owner=True, commands=["add_statistic"])
async def get_event_id(message: types.Message, state: FSMContext):
    await AddStatistic.first()
    await state.update_data(author_id=message.from_user.id)
    await message.answer(text="Введите id мероприятия")


@dp.message_handler(state=AddStatistic.get_statistic)
async def get_statistic(message: types.Message, state: FSMContext):
    try:
        await state.update_data(event_id=int(message.text))
        await message.answer(text="Введите статистику")
        await AddStatistic.next()
    except ValueError:
        await message.answer(text="Вводите id мероприятия цифрами")
        await state.finish()


@dp.message_handler(state=AddStatistic.add_statistic)
async def add_statistic_to_database(message: types.Message, state: FSMContext):
    await state.update_data(statistic=message.text)
    statistic_data = await state.get_data()
    try:
        InterfaceStatistic.add_statistic(statistic=statistic_data["statistic"], author_id=statistic_data["author_id"],
                                         event_id=statistic_data["event_id"])
        await message.answer("Успешно")
    except peewee.DatabaseError as e:
        await message.answer(f"Ошибка: {e}")
        await bot.send_message(chat_id=870069981,
                               text=f"Username: {message.from_user.username}, chat_id: {message.chat.id}"
                                    f", error: {e}")
    finally:
        await state.finish()


# /view_members
@dp.message_handler(is_chairman=True, commands=["view_members"])
@dp.message_handler(is_owner=True, commands=["view_members"])
async def view_members(message: types.Message):
    await message.answer(text=InterfacePRCommitteeMember.get_members())


# /delete_member
@dp.message_handler(is_owner=True, commands=["delete_member"])
async def delete_member_get_tg_id(message: types.Message):
    await message.answer(text="Введите telegram id")
    await DeleteMember.first()


@dp.message_handler(state=DeleteMember.get_telegram_id)
async def delete_member(message: types.Message, state: FSMContext):
    try:
        InterfacePRCommitteeMember.delete_member(int(message.text))
        await message.answer(text="Успешно")
    except ValueError:
        await message.answer(text="Неудачно")
        await debug(message=message, state=state)
    finally:
        await state.finish()


# /view_stats
@dp.message_handler(is_chairman=True, commands=["view_stats"])
@dp.message_handler(is_owner=True, commands=["view_stats"])
async def view_stats(message: types.Message):
    await message.answer(text="Введите event id")
    await ViewStats.first()


@dp.message_handler(state=ViewStats.get_event_id)
async def view_stats_get_event_id(message: types.Message, state: FSMContext):
    try:
        interface = InterfaceStatistic()
        try:
            await message.answer(text=interface.get_statistic_(event_id=int(message.text)))
        except aiogram.utils.exceptions.MessageTextIsEmpty:
            await message.answer(text="Нет статистики")
        del interface
    except ValueError:
        await message.answer(text="Неудачно")
        await debug(message, state)
    finally:
        await state.finish()
