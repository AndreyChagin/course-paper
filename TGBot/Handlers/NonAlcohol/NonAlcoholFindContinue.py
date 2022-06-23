from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import cocktail_list, OutputManual, data
from TGBot.State.Answer2 import Answer2


class ContinueFind:
    """ Класс отвечающий за продолжение поиска безалкогольных коктейлей """
    @staticmethod
    async def no_yes(message: types.Message, state: FSMContext):
        """ Хендлер отвечающий за продолжение поиска безалкогольных коктейлей """
        if message.text.lower() == "нет":
            await message.answer(f'Спасибо что зашли к нам, приятного вечера, {message.from_user.first_name}')
            await state.finish()
        elif message.text.lower() == "да":

            count = 0
            max_cocktail = 3
            for x in cocktail_list.get_random_cocktail_list():
                if 'безалкогольные' in data[x]['Tags']:
                    await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                         f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                         f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                         f'<i>Рецепт:</i>\n'
                                         f'{OutputManual(data[x]["Manual"]).output_manual}'
                                         f'', parse_mode='html')
                    count += 1
                if count == max_cocktail:
                    await message.answer('Хочешь, хочешь и молчишь?')
                    break
            if count < max_cocktail:
                await message.answer('Конец, попробуйте заново')
        else:
            await message.answer('Ты по-моему перепутал')

    @staticmethod
    def register_handler_nonalcohol_find_continue(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(ContinueFind.no_yes, state=Answer2.answer2)
