from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import data, get_index_cocktail, OutputManual
from TGBot.State.Answer import Answer


class AlcoholAnswer:
    """ Класс отвечающий за продолжение поиска алкогольных коктейлей """
    @staticmethod
    async def no_yes(message: types.Message, state: FSMContext):
        """ Хендлер отвечающий за продолжение поиска алкогольных коктейлей """
        if message.text.lower() == "нет":
            await message.answer(f'Спасибо что зашли ко мне, приятного вечера, {message.from_user.first_name}')
            await state.finish()
        elif message.text.lower() == 'да':

            count = 0
            max_cocktail = 3

            for x in get_index_cocktail():
                if 'безалкогольные' not in data[x]['Tags']:
                    await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                         f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                         f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                         f'<i>Рецепт:</i>\n'
                                         f'{OutputManual(data[x]["Manual"]).output_manual}',
                                         parse_mode='html')
                    count += 1
                if count == max_cocktail:
                    await message.answer('Хочешь, хочешь и молчишь?')
                    break
            if count < max_cocktail:
                await message.answer('Конец, попробуйте заново')
        else:
            await message.answer('Ты по-моему перепутал')

    @staticmethod
    def register_handler_alcohol_find_continue(dp: Dispatcher):
        """ Функция регистрации хендлера """
        dp.register_message_handler(AlcoholAnswer.no_yes, state=Answer.answer)
