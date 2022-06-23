from aiogram.utils import executor

from TGBot.ConfigTGBot.TGBotsettings import TGBotConfig
from .Handlers import *


class TGBOt:
    """ Запуск всех хендлеров и самого бота"""
    StartTG.register_handler_start(TGBotConfig.dp)
    MesAlcohol.register_handler_alcohol_find(TGBotConfig.dp)
    AlcoholAnswer.register_handler_alcohol_find_continue(TGBotConfig.dp)
    SearchNonalcohol.register_handler_nonalcohol_find(TGBotConfig.dp)
    ContinueFind.register_handler_nonalcohol_find_continue(TGBotConfig.dp)
    SearchRandomCocktail.register_handler_random_cocktail(TGBotConfig.dp)
    NameInput.register_handler_input_name(TGBotConfig.dp)
    SearchCocktail.register_handler_search_name_cocktail(TGBotConfig.dp)
    InputTags.register_handler_input_tags(TGBotConfig.dp)
    FindForTags.register_handler_find_for_tags(TGBotConfig.dp)
    ContinueFindForTg.register_handler_continue_find_for_tags(TGBotConfig.dp)
    HelpBot.register_handler_help(TGBotConfig.dp)

    executor.start_polling(TGBotConfig.dp, skip_updates=True)
