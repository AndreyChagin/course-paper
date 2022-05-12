import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import cocktail
from State.Answer2 import Answer2


class SearchNonalcohol:
    @staticmethod
    async def mes(message: types.Message):
        await message.answer(f'Ожидайте, {message.from_user.first_name}')
        await asyncio.sleep(2)

        count = 0
        for x in cocktail.cocktail_list.get_random_cocktail_list():
            if message.text.lower() in cocktail.cocktail_list.data[x]['Tags'] and message.text.lower() == 'безалкогольные':
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
                await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
            if count == 3:
                break
        if count < 3:
            await message.answer('Конец, попробуйте заново')
        await message.answer('Еще хотите? (да/нет)')
        await Answer2.answer2.set()

    @staticmethod
    def register_handler_nonalcohol_find(dp: Dispatcher):
        dp.register_message_handler(SearchNonalcohol.mes, Text(equals='Безалкогольные'), state=None)
