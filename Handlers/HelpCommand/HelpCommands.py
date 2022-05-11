from aiogram import types, Dispatcher


async def help_bot(message: types.Message):
    await message.answer('/start - запуск бота')


def register_handler_help(dp: Dispatcher):
    dp.register_message_handler(help_bot, commands='help')

