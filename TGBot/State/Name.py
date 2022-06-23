from aiogram.dispatcher.filters.state import StatesGroup, State


class Name(StatesGroup):
    """ Создание машинного состояния для поиска коктейлей по наименованию """
    answer_name = State()
