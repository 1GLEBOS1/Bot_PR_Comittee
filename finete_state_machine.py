from aiogram.dispatcher.filters.state import State, StatesGroup


class AddMember(StatesGroup):
    get_telegram_id = State()
    get_name = State()
    get_access_level = State()
    get_position = State()
