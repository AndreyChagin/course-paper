from aiogram import types, Dispatcher


class HelpBot:
    """ Класс отвечающий за команду help """
    @staticmethod
    async def help_bot(message: types.Message):
        """ Хендлер обрабатывающий команду help"""
        await message.answer('/start - запуск бота')

    @staticmethod
    def register_handler_help(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(HelpBot.help_bot, commands='help')
