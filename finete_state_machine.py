from aiogram.dispatcher.filters.state import State, StatesGroup


class AddMember(StatesGroup):
    get_telegram_id = State()
    get_name = State()
    get_access_level = State()
    get_position = State()


class ViewStatistic(StatesGroup):
    get_event_id = State()


class AddStatistic(StatesGroup):
    get_statistic = State()
    add_statistic = State()


class DeleteMember(StatesGroup):
    get_telegram_id = State()


class ViewStats(StatesGroup):
    get_event_id = State()


class ChangeAuthorId(StatesGroup):
    get_id = State()
    get_author_id = State()


class DeleteStatistic(StatesGroup):
    get_id = State()
