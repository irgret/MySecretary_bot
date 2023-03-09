import requests
import datetime
from aiogram import types
# from pprint import pprint
from config import open_weather_token
from aiogram.types import ReplyKeyboardRemove
from create_bot import dp, bot

import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode


class Form(StatesGroup):
    name = State()

# @dp.message_handler(Text(equals='Узнать погоду', ignore_case=True))
async def cmd_weather(message : types.Message):
    await Form.name.set()
    await message.answer('Введите город: ', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

        await bot.send_message(
            message.chat.id,
            md.text('Прогноз на сегодня:', md.bold(data['name'])), parse_mode=ParseMode.MARKDOWN
        )

        code_to_smile = {
            'Thunderstorm': 'Гроза \U000026C8',
            'Drizzle': 'Моросящий дождь \U00002600',
            'Rain': 'Дождь \U00002614',
            'Snow': 'Снег \U00002744',
            'Mist': 'Туман \U0001F32B',
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U000026C5'
        }

        try:
            r = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
            )
            data = r.json()
            # pprint(data)

            true_city = data['name']
            cur_weather = round(data['main']['temp'])

            weather_description = data['weather'][0]['main']
            if weather_description in code_to_smile:
                weather = code_to_smile[weather_description]
            else:
                weather = 'Посмотри в окно, не могу понять, что там'

            humidity = data['main']['humidity']
            pressure = round(data['main']['pressure']*0.750063755419211)
            wind = round(data['wind']['speed'], 1)
            sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

            await message.reply(f'Погода в городе: {true_city}\nТемпература: {cur_weather} C°\nЗа окном: {weather}\n'
                                f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
                                )
                                #f'Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}'
                            

        except:
            await message.reply('Проверьте название города')

        await state.finish()



