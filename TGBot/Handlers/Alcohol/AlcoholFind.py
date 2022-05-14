import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from Cocktail import cocktail_list, OutputManual
from TGBot.State.Answer import Answer


class MesAlcohol:
    @staticmethod
    async def mes(message: types.Message):
        await message.answer(f'Ожидайте, {message.from_user.first_name}')
        await asyncio.sleep(2)

        count = 0

        for x in cocktail_list.get_random_cocktail_list():
            if message.text.lower() not in cocktail_list.data[x]['Tags']:
                await message.answer(f'<u><b>{cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n'
                                     f'{OutputManual(cocktail_list.data[x]["Manual"]).output_manual}',
                                     parse_mode='html')
                count += 1
            if count == 3:
                break
        if count < 3:
            await message.answer('Конец, попробуйте заново')
        await message.answer('Еще хотите? (да/нет)')
        await Answer.answer.set()

    @staticmethod
    def register_handler_alcohol_find(dp: Dispatcher):
        dp.register_message_handler(MesAlcohol.mes, Text(equals='Алкогольные'), state=None)
