from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from TGBot.State.Name import Name


class NameInput:
    """ Класс отвечающий за ввод наименования коктейля """
    @staticmethod
    async def name(message: types.Message):
        """ Хендлер для ввода наименования коктейля """
        await message.answer(f'Введите наименование коктейля, {message.from_user.first_name}')
        await Name.answer_name.set()

    @staticmethod
    def register_handler_input_name(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(NameInput.name, Text(equals='По наименованию'))
