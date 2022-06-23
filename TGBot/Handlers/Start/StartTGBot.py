from aiogram import types
from aiogram import Dispatcher


class StartTG:
    """ Класс отвечающий за команду start """
    @staticmethod
    async def start(message: types.Message):
        """ Хендлер обработки команды start """
        start_button = ['Алкогольные', 'Безалкогольные', 'Рандомный напиток', 'По наименованию', 'По тегу']
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key.add(*start_button)
        await message.answer(f'Можете выбирать', reply_markup=key)

    @staticmethod
    def register_handler_start(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(StartTG.start, commands='start')
