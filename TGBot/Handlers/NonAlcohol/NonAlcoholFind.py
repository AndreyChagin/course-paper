from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from Cocktail import data, get_index_cocktail, OutputManual
from TGBot.State.Answer2 import Answer2


class SearchNonalcohol:
    """ Класс отвечающий за поиск безалкогольных коктейлей """
    @staticmethod
    async def mes(message: types.Message):
        """ Хендлер поиска безалкогольных коктейлей """
        count = 0
        max_cocktail = 3

        for x in get_index_cocktail():
            if message.text.lower() in data[x]['Tags'] and message.text.lower() == 'безалкогольные':
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n'
                                     f'{OutputManual(data[x]["Manual"]).output_manual}',
                                     parse_mode='html')
                count += 1
            if count == max_cocktail:
                break
        if count < max_cocktail:
            await message.answer('Конец, попробуйте заново')
        await message.answer('Еще хотите? (да/нет)')
        await Answer2.answer2.set()

    @staticmethod
    def register_handler_nonalcohol_find(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(SearchNonalcohol.mes, Text(equals='Безалкогольные'))
