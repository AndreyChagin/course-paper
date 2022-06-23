from aiogram.dispatcher.filters.state import StatesGroup, State


class Tags(StatesGroup):
    """ Создание машинного состояния для поиска коктейля по тегу """
    answer_tag_user = State()
    answer_tag_user_2 = State()
