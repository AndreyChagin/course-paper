from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from State.Name import Name


async def name(message: types.Message):
    await message.answer(f'Введите наименование коктейля, {message.from_user.first_name}')
    await Name.answer_name.set()

def register_handler_input_name(dp: Dispatcher):
    dp.register_message_handler(name, Text(equals='По наименованию'), state=None)
