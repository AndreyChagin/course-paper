import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from Cocktail import cocktail_list, OutputManual


class SearchRandomCocktail:
    @staticmethod
    async def mes(message: types.Message):

        count = random.randint(0, 949)
        data = cocktail_list.data
        await message.answer(f'<u><b>{data[count]["Name"].upper().strip()}</b></u>\n\n'
                             f'<i>Ингредиенты:</i>\n{data[count]["Ingredients"]}\n\n'
                             f'<i>Инструменты:</i>\n{data[count]["Tools"]}\n\n'
                             f'<i>Рецепт:</i>\n'
                             f'{OutputManual(data[count]["Manual"]).output_manual}',
                             parse_mode='html')

    @staticmethod
    def register_handler_random_cocktail(dp: Dispatcher):
        dp.register_message_handler(SearchRandomCocktail.mes, Text(equals='Рандомный напиток'))
