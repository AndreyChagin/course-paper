from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    """ Создание машинного состояния для тега алкогольные """
    answer = State()
