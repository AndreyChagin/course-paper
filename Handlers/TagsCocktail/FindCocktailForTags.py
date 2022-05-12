from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import cocktail
from State.Tags import Tags


class FindForTags:
    @staticmethod
    async def tags_find(message: types.Message, state: FSMContext):
        item = set(message.text.lower().split(', '))
        await state.update_data(
            {
                'answer_tag_user': item
            }
        )

        count = 0
        for x in cocktail.cocktail_list.get_random_cocktail_list():
            if set(message.text.lower().split(', ')).issubset(cocktail.cocktail_list.data[x]['Tags'].split(' / ')):
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
                await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
                if count == 4:
                    await message.answer('Продолжаем?(да/нет)')
                    await Tags.next()
                    break
        if count == 0:
            await message.answer('Такого тега нет!!!\nВы вышли из категории <i>По тегу</i>', parse_mode='html')
            await state.finish()
        elif count < 4:
            await message.answer('Это все коктейли по данному тегу!!!')
            await state.finish()

    @staticmethod
    def register_handler_find_for_tags(dp: Dispatcher):
        dp.register_message_handler(FindForTags.tags_find, state=Tags.answer_tag_user)
