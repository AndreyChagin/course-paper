import asyncio
import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from Cocktail import cocktail_list, OutputManual


class SearchRandomCocktail:
    @staticmethod
    async def mes(message: types.Message):
        await message.answer(f'Ожидайте, {message.from_user.first_name}')
        await asyncio.sleep(2)

        count = random.randint(0, 949)
        await message.answer(f'<u><b>{cocktail_list.data[count]["Name"].upper().strip()}</b></u>\n\n'
                             f'<i>Ингредиенты:</i>\n{cocktail_list.data[count]["Ingredients"]}\n\n'
                             f'<i>Инструменты:</i>\n{cocktail_list.data[count]["Tools"]}\n\n'
                             f'<i>Рецепт:</i>\n'
                             f'{OutputManual(cocktail_list.data[count]["Manual"]).output_manual}',
                             parse_mode='html')

    @staticmethod
    def register_handler_random_cocktail(dp: Dispatcher):
        dp.register_message_handler(SearchRandomCocktail.mes, Text(equals='Рандомный напиток'))
