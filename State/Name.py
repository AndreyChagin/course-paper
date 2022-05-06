from aiogram.dispatcher.filters.state import StatesGroup, State


class Name(StatesGroup):
    answer_name = State()
