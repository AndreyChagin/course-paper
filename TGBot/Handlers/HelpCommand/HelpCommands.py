from aiogram import types, Dispatcher


class HelpBot:
    @staticmethod
    async def help_bot(message: types.Message):
        await message.answer('/start - запуск бота')

    @staticmethod
    def register_handler_help(dp: Dispatcher):
        dp.register_message_handler(HelpBot.help_bot, commands='help')
