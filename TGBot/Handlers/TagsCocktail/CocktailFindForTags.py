from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import data, get_index_cocktail, OutputManual
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
        max_cocktail = 4
        for x in get_index_cocktail():
            if set(message.text.lower().split(', ')).issubset(data[x]['Tags'].split(' / ')):
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>'
                                     f'\n{OutputManual(data[x]["Manual"]).output_manual}',
                                     parse_mode='html')
                count += 1
                if count ==  max_cocktail:
                    await message.answer('Продолжаем?(да/нет)')
                    await Tags.next()
                    break
        if count == 0:
            await message.answer('Такого тега нет!!!\nВы вышли из категории <i>По тегу</i>', parse_mode='html')
            await state.finish()
        elif count < max_cocktail:
            await message.answer('Это все коктейли по данному тегу!!!')
            await state.finish()

    @staticmethod
    def register_handler_find_for_tags(dp: Dispatcher):
        dp.register_message_handler(FindForTags.tags_find, state=Tags.answer_tag_user)
