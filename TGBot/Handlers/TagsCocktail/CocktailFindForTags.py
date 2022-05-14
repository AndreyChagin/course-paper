from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import cocktail_list, OutputManual
from TGBot.State.Tags import Tags


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
        for x in cocktail_list.get_random_cocktail_list():
            if set(message.text.lower().split(', ')).issubset(cocktail_list.data[x]['Tags'].split(' / ')):
                await message.answer(f'<u><b>{cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>'
                                     f'\n{OutputManual(cocktail_list.data[x]["Manual"]).output_manual}',
                                     parse_mode='html')
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
