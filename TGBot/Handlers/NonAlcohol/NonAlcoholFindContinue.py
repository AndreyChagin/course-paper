from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import cocktail_list
from TGBot.State.Answer2 import Answer2


class ContinueFind:
    @staticmethod
    async def no_yes(message: types.Message, state: FSMContext):
        if message.text.lower() == "нет":
            await message.answer(f'Спасибо что зашли к нам, приятного вечера, {message.from_user.first_name}')
            await state.finish()
        elif message.text.lower() == "да":

            count = 0
            for x in cocktail_list.get_random_cocktail_list():
                if 'безалкогольные' in cocktail_list.data[x]['Tags']:
                    output_string_manual = "\n".join(
                        [str(key) + ". " + str(value) for key, value in cocktail_list.data[x]["Manual"].items()])
                    await message.answer(f'<u><b>{cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                         f'<i>Ингредиенты:</i>\n{cocktail_list.data[x]["Ingredients"]}\n\n'
                                         f'<i>Инструменты:</i>\n{cocktail_list.data[x]["Tools"]}\n\n'
                                         f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                    count += 1
                if count == 3:
                    await message.answer('Хочешь, хочешь и молчишь?')
                    break
            if count < 3:
                await message.answer('Конец, попробуйте заново')
        else:
            await message.answer('Ты по-моему перепутал')

    @staticmethod
    def register_handler_nonalcohol_find_continue(dp: Dispatcher):
        dp.register_message_handler(ContinueFind.no_yes, state=Answer2.answer2)