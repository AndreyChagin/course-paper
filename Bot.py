import asyncio
from aiogram import Dispatcher, executor, types, Bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
from data import set_tags, data, lst


class Answer(StatesGroup):
    answer = State()


class Answer2(StatesGroup):
    answer2 = State()


class Name(StatesGroup):
    answer_name = State()


class Tags(StatesGroup):
    answer_tag_user = State()
    answer_tag_user_2 = State()


bot = Bot('5302483007:AAEiZojd-OQ3kx_smKhyAPeL7C39EoRlmm4')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


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

    for x in lst:
        if message.text.lower() not in data[x]['Tags']:
            output_string_manual = "\n".join([str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
            await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                 f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
            count += 1
        if count == 3:
            break
    await message.answer('Еще хотите? (да/нет)')
    await Answer.answer.set()


@dp.message_handler(state=Answer.answer)
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

        for x in lst:
            if 'безалкогольные' not in data[x]['Tags']:
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
            if count == 3:

                await message.answer('Хочешь, хочешь и молчишь?')
                break
    else:
        await message.answer('Ты по-моему перепутал')


@dp.message_handler(Text(equals='Безалкогольные'), state=None)
async def mes(message: types.Message):
    await message.answer(f'Ожидайте, {message.from_user.first_name}')
    await asyncio.sleep(2)

    count = 0
    for x in lst:
        if message.text.lower() in data[x]['Tags'] and message.text.lower() == 'безалкогольные':
            output_string_manual = "\n".join(
                [str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
            await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                 f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
            count += 1
        if count == 3:
            break
    await message.answer('Еще хотите? (да/нет)')
    await Answer2.answer2.set()


@dp.message_handler(state=Answer2.answer2)
async def no_yes(message: types.Message, state: FSMContext):
    if message.text.lower() == "нет":
        await message.answer(f'Спасибо что зашли к нам, приятного вечера, {message.from_user.first_name}')
        await state.finish()
    elif message.text.lower() == "да":

        count = 0
        for x in lst:
            if ' безалкогольные' in data[x]['Tags']:
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
                                     f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')
                count += 1
            if count == 3:
                await message.answer('Хочешь, хочешь и молчишь?')
                break
    else:
        await message.answer('Ты по-моему перепутал')


@dp.message_handler(Text(equals='Рандомный напиток'))
async def mes(message: types.Message):
    await message.answer(f'Ожидайте, {message.from_user.first_name}')
    await asyncio.sleep(2)

    count = random.randint(0, 949)
    output_string_manual = "\n".join(
        [str(key) + ". " + str(value) for key, value in data[count]["Manual"].items()])
    await message.answer(f'<u><b>{data[count]["Name"].upper().strip()}</b></u>\n\n'
                         f'<i>Ингредиенты:</i>\n{data[count]["Ingredients"]}\n\n'
                         f'<i>Инструменты:</i>\n{data[count]["Tools"]}\n\n'
                         f'<i>Рецепт:</i>\n{output_string_manual}', parse_mode='html')


@dp.message_handler(Text(equals='По наименованию'), state=None)
async def name(message: types.Message):
    await message.answer(f'Введите наименование коктейля, {message.from_user.first_name}')
    await Name.answer_name.set()


@dp.message_handler(state=Name.answer_name)
async def name_find(message: types.Message, state: FSMContext):
    for item in data:
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

    await message.answer(f'<i>{set_tags}</i>', parse_mode='html')
    await message.answer('Введите тег(и), через -> ", "')
    await Tags.answer_tag_user.set()


@dp.message_handler(state=Tags.answer_tag_user)
async def tags_find(message: types.Message, state: FSMContext):
    item = set(message.text.lower().split(', '))
    await state.update_data(
        {
            'answer_tag_user': item
        }
    )

    count = 0
    for x in lst:
        if set(message.text.lower().split(', ')).issubset(data[x]['Tags'].strip().split(' /  ')):
            output_string_manual = "\n".join(
                [str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
            await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                 f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                 f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
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


@dp.message_handler(state=Tags.answer_tag_user_2)
async def answer_tag_2(message: types.Message, state: FSMContext):
    item_tags = await state.get_data()
    if message.text.lower() == 'да':

        count = 0
        for x in lst:
            if item_tags.get('answer_tag_user').issubset(data[x]['Tags'].strip().split(' /  ')):
                output_string_manual = "\n".join(
                    [str(key) + ". " + str(value) for key, value in data[x]["Manual"].items()])
                await message.answer(f'<u><b>{data[x]["Name"].upper().strip()}</b></u>\n\n'
                                     f'<i>Ингредиенты:</i>\n{data[x]["Ingredients"]}\n\n'
                                     f'<i>Инструменты:</i>\n{data[x]["Tools"]}\n\n'
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
