
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from Cocktail import data, get_index_cocktail, OutputManual
from TGBot.State.Answer import Answer


class MesAlcohol:
    @staticmethod
    async def mes(message: types.Message):

        count = 0
        max_cocktail = 3

        for x in get_index_cocktail():
            if message.text.lower() not in data[x]['Tags']:
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n'
                                     f'{OutputManual(data[x]["Manual"]).output_manual}'
                                     f'\n{id(data)}',
                                     parse_mode='html')
                count += 1
            if count == max_cocktail:
                break
        if count < max_cocktail:
            await message.answer('Конец, попробуйте заново')
        await message.answer('Еще хотите? (да/нет)')
        await Answer.answer.set()

    @staticmethod
    def register_handler_alcohol_find(dp: Dispatcher):
        dp.register_message_handler(MesAlcohol.mes, Text(equals='Алкогольные'))
