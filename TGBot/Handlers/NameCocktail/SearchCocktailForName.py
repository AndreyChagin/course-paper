from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import data, OutputManual
from TGBot.State.Name import Name


class SearchCocktail:
    """ Класс отвечающий за поиск коктейля по наименованию """
    @staticmethod
    async def name_find(message: types.Message, state: FSMContext):
        """ Хендлер поиска коктейля по наименованию """
        msg = message.text.lower().replace('ё', 'е')
        for item in data:
            if msg in item['Name'].lower():
                await message.answer(f'<u><b>{item["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{item["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{item["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n'
                                     f'{OutputManual(item["Manual"]).output_manual}',
                                     parse_mode='html')
                break
        else:
            await message.answer('Я такого коктейля не знаю!!!')
        await state.finish()

    @staticmethod
    def register_handler_search_name_cocktail(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(SearchCocktail.name_find, state=Name.answer_name)
