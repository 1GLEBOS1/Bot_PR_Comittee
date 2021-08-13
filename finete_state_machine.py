from aiogram.dispatcher.filters.state import State, StatesGroup


class AddMember(StatesGroup):
    get_telegram_id = State()
    get_name = State()
    get_access_level = State()
    get_position = State()


class ViewStatistic(StatesGroup):
    get_event_id = State()


class AddStatisticAuto(StatesGroup):
    get_statistic = State()
    add_statistic_publics = State()
    add_statistic_publics_all = State()
    add_statistic_publics_responsed = State()
    add_statistic_publics_registered = State()
    add_statistic_familiar = State()
    add_statistic_familiar_all = State()
    add_statistic_familiar_responsed = State()
    add_statistic_familiar_registered = State()
    add_statistic_to_database = State()


class AddStatisticManually(StatesGroup):
    get_event_id = State()
    get_statistic = State()


class DeleteMember(StatesGroup):
    get_telegram_id = State()


class ViewStatsEevnt(StatesGroup):
    get_event_id = State()


class ViewStatsAuthor(StatesGroup):
    get_author_id = State()


class ChangeAuthorId(StatesGroup):
    get_id = State()
    get_author_id = State()


class DeleteStatistic(StatesGroup):
    get_id = State()
