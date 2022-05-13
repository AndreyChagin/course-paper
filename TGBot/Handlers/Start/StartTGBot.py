from aiogram import types
from aiogram import Dispatcher

class StartTG:
    async def start(message: types.Message):
        start_button = ['Алкогольные', 'Безалкогольные', 'Рандомный напиток', 'По наименованию', 'По тегу']
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key.add(*start_button)
        await message.answer(f'Можете выбирать', reply_markup=key)

    @staticmethod
    def register_handler_start(dp: Dispatcher):
        dp.register_message_handler(StartTG.start, commands='start')

