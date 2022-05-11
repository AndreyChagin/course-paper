from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import cocktail
from State.Answer import Answer


async def no_yes(message: types.Message, state: FSMContext):
    item = message.text
    await state.update_data(
        {
            'answer': item
        }
    )
    rez = await state.get_data()
    rez_out = str(rez.get('answer'))
    if rez_out.lower() == "нет":
        await message.answer(f'Спасибо что зашли ко мне, приятного вечера, {message.from_user.first_name}')
        await state.finish()
    elif rez_out.lower() == 'да':

        count = 0

        for x in cocktail.cocktail_list.get_random_cocktail_list():
            if 'безалкогольные' not in cocktail.cocktail_list.data[x]['Tags']:
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
                await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
            if count == 3:

                await message.answer('Хочешь, хочешь и молчишь?')
                break
        if count < 3:
            await message.answer('Конец, попробуйте заново')
    else:
        await message.answer('Ты по-моему перепутал')

def register_handler_alcohol_find_continue(dp: Dispatcher):
    dp.register_message_handler(no_yes, state=Answer.answer)
