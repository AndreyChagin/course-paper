import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import cocktail
from State.Tags import Tags


class InputTags:
    @staticmethod
    async def tags_input(message: types.Message):
        await message.answer(
            f'Так, {message.from_user.first_name}, я знаю около 85 тегов коктейлей.\n'
            f'Минутку ожидания, идет сбор информации')
        await asyncio.sleep(3)

        await message.answer(f'<i>{cocktail.Cocktail_list_render.CocktailRenderList.show_tags(cocktail.cocktail_list.get_list_tags)}'
                             f'</i>', parse_mode='html')
        await message.answer('Введите тег(и), через -> ", "')
        await Tags.answer_tag_user.set()

    @staticmethod
    def register_handler_input_tags(dp: Dispatcher):
        dp.register_message_handler(InputTags.tags_input, Text(equals='По тегу'), state=None)
