import asyncio
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import random

import cocktail
from State import Answer, Answer2, Name, Tags
from TgBot_config.config import dp


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_button = ['Алкогольные', 'Безалкогольные', 'Рандомный напиток', 'По наименованию', 'По тегу']
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(*start_button)
    await message.answer(f'Можете выбирать', reply_markup=key)


@dp.message_handler(Text(equals='Алкогольные'), state=None)
async def mes(message: types.Message):
    await message.answer(f'Ожидайте, {message.from_user.first_name}')
    await asyncio.sleep(2)

    count = 0

    for x in cocktail.cocktail_list.get_random_cocktail_list():
        if message.text.lower() not in cocktail.cocktail_list.data[x]['Tags']:
            output_string_manual = "\n".join([str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
            await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                 f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
            count += 1
        if count == 3:
            break
    if count < 3:
        await message.answer('Конец, попробуйте заново')
    await message.answer('Еще хотите? (да/нет)')
    await Answer.Answer.answer.set()


@dp.message_handler(state=Answer.Answer.answer)
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


@dp.message_handler(Text(equals='Безалкогольные'), state=None)
async def mes(message: types.Message):
    await message.answer(f'Ожидайте, {message.from_user.first_name}')
    await asyncio.sleep(2)

    count = 0
    for x in cocktail.cocktail_list.get_random_cocktail_list():
        if message.text.lower() in cocktail.cocktail_list.data[x]['Tags'] and message.text.lower() == 'безалкогольные':
            output_string_manual = "\n".join(
                [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
            await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                 f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
            count += 1
        if count == 3:
            break
    if count < 3:
        await message.answer('Конец, попробуйте заново')
    await message.answer('Еще хотите? (да/нет)')
    await Answer2.Answer2.answer2.set()


@dp.message_handler(state=Answer2.Answer2.answer2)
async def no_yes(message: types.Message, state: FSMContext):
    if message.text.lower() == "нет":
        await message.answer(f'Спасибо что зашли к нам, приятного вечера, {message.from_user.first_name}')
        await state.finish()
    elif message.text.lower() == "да":

        count = 0
        for x in cocktail.cocktail_list.get_random_cocktail_list():
            if 'безалкогольные' in cocktail.cocktail_list.data[x]['Tags']:
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


@dp.message_handler(Text(equals='Рандомный напиток'))
async def mes(message: types.Message):
    await message.answer(f'Ожидайте, {message.from_user.first_name}')
    await asyncio.sleep(2)

    count = random.randint(0, 949)
    output_string_manual = "\n".join(
        [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[count]["Manual"].items()])
    await message.answer(f'<u><b>{cocktail.cocktail_list.data[count]["Name"].upper().strip()}</b></u>\n\n'
                         f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[count]["Ingredients"]}\n\n'
                         f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[count]["Tools"]}\n\n'
                         f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')


@dp.message_handler(Text(equals='По наименованию'), state=None)
async def name(message: types.Message):
    await message.answer(f'Введите наименование коктейля, {message.from_user.first_name}')
    await Name.Name.answer_name.set()


@dp.message_handler(state=Name.Name.answer_name)
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


@dp.message_handler(Text(equals='По тегу'), state=None)
async def tags_find(message: types.Message):
    await message.answer(
        f'Так, {message.from_user.first_name}, я знаю около 85 тегов коктейлей.\n'
        f'Минутку ожидания, идет сбор информации')
    await asyncio.sleep(3)

    await message.answer(f'<i>{cocktail.Cocktail_list_render.CocktailRenderList.show_tags(cocktail.cocktail_list.get_list_tags)}'
                         f'</i>', parse_mode='html')
    await message.answer('Введите тег(и), через -> ", "')
    await Tags.Tags.answer_tag_user.set()


@dp.message_handler(state=Tags.Tags.answer_tag_user)
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
                await Tags.Tags.next()
                break
    if count == 0:
        await message.answer('Такого тега нет!!!\nВы вышли из категории <i>По тегу</i>', parse_mode='html')
        await state.finish()
    elif count < 4:
        await message.answer('Это все коктейли по данному тегу!!!')
        await state.finish()


@dp.message_handler(state=Tags.Tags.answer_tag_user_2)
async def answer_tag_2(message: types.Message, state: FSMContext):
    item_tags = await state.get_data()
    if message.text.lower() == 'да':

        count = 0
        for x in cocktail.cocktail_list.__lst_tags__:
            if item_tags.get('answer_tag_user').issubset(cocktail.cocktail_list.data[x]['Tags'].split(' / ')):
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in cocktail.cocktail_list.data[x]["Manual"].items()])
                await message.answer(f'<u><b>{cocktail.cocktail_list.data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{cocktail.cocktail_list.data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{cocktail.cocktail_list.data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
            if count == 3:
                await message.answer('Еще или хватит?(да/нет)')
                break
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer(f'Спасибо что зашли ко мне, хорошего вечера, {message.from_user.first_name}')
    else:
        await message.answer('<u><b>Проверьте правильность веденного</b></u>', parse_mode='html')


@dp.message_handler(commands='help')
async def help_bot(message: types.Message):
    await message.answer('/start - запуск бота')



