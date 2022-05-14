from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Cocktail import cocktail_list, OutputManual
from TGBot.State.Tags import Tags


class ContinueFindForTg:
    @staticmethod
    async def answer_tag_2(message: types.Message, state: FSMContext):
        item_tags = await state.get_data()
        if message.text.lower() == 'да':

            count = 0
            for x in cocktail_list.get_random_cocktail_list():
                if item_tags.get('answer_tag_user').issubset(cocktail_list.data[x]['Tags'].split(' / ')):
                    await message.answer(f'<u><b>{cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                         f'<i>Ингредиенты:</i>\n{cocktail_list.data[x]["Ingredients"]}\n\n'
                                         f'<i>Инструменты:</i>\n{cocktail_list.data[x]["Tools"]}\n\n'
                                         f'<i>Рецепт:</i>'
                                         f'\n{OutputManual(cocktail_list.data[x]["Manual"]).output_manual}',
                                         parse_mode='html')
                    count += 1
                if count == 3:
                    await message.answer('Еще или хватит?(да/нет)')
                    break
        elif message.text.lower() == 'нет':
            await state.finish()
            await message.answer(f'Спасибо что зашли ко мне, хорошего вечера, {message.from_user.first_name}')
        else:
            await message.answer('<u><b>Проверьте правильность веденного</b></u>', parse_mode='html')

    @staticmethod
    def register_handler_continue_find_for_tags(dp: Dispatcher):
        dp.register_message_handler(ContinueFindForTg.answer_tag_2, state=Tags.answer_tag_user_2)
