from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from TGBot.ConfigTGBot import settings


class TGBotConfig:
    """ Создание объекта бота и обработчика событий """
    bot = Bot(token=str(settings.BOT_TOKEN))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
