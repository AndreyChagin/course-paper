from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configTGBot import settings

class TGBotConfig:
    bot = Bot(token=str(settings.BOT_TOKEN))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
