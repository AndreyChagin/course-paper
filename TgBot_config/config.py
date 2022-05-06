from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from TgBot_config import settings

bot = Bot(token=str(settings.BOT_TOKEN))
dp = Dispatcher(bot, storage=MemoryStorage())
