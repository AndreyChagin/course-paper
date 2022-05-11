from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import cocktail
from State.Name import Name


async def name_find(message: types.Message, state: FSMContext):
    for item in cocktail.cocktail_list.data:
        if message.text.lower().replace('ё', 'е') in item['Name'].lower():
            output_string_manual = "\n".join(
                [str(key) + ". " + str(value) for key, value in item["Manual"].items()])
            await message.answer(f'<u><b>{item["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{item["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{item["Tools"]}\n\n'
                                 f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
            break
    else:
        await message.answer('Я такого коктейля не знаю ¯\_(ツ)_/¯')
    await state.finish()


def register_handler_search_name_cocktail(dp: Dispatcher):
    dp.register_message_handler(name_find, state=Name.answer_name)
