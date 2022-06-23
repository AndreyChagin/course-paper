from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer2(StatesGroup):
    """ Создание машинного состояния для тега безалкогольные """
    answer2 = State()
