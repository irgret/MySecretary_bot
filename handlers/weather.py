import requests
import datetime
from aiogram import types
# from pprint import pprint
from config import open_weather_token
from create_bot import dp, bot
from keyboards.kb_inline import inkb_weather
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup



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
        global city_name
        city_name = data['name']
        await state.finish()
        await bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=inkb_weather)



@dp.callback_query_handler(Text(startswith='weather_'))
async def button_call(callback : types.CallbackQuery):
    res = callback.data.split('_')[1]
    code_to_smile = {
            'Thunderstorm': 'Гроза \U000026C8',
            'Drizzle': 'Моросящий дождь \U00002600',
            'Rain': 'Дождь \U00002614',
            'Snow': 'Снег \U00002744',
            'Mist': 'Туман \U0001F32B',
            'Clear': 'Ясно \U00002600',
            'Clouds': 'Облачно \U000026C5'
    }

    if res == 'today':
        await callback.message.answer(
            md.text('Прогноз на сегодня:', md.bold(city_name)), parse_mode=ParseMode.MARKDOWN
        )

        try:
            r = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_token}&units=metric'
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

            await callback.message.answer(f'Погода в городе: {true_city}\nТемпература: {cur_weather} C°\nЗа окном: {weather}\n'
                                f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
                                )
                                #f'Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}'
            await callback.answer(show_alert=False)
                        

        except:
            await callback.answer('Проверьте название города', show_alert=True)


    elif res == 'forecast':
        await callback.message.answer(
            md.text('Прогноз на 5 дней:', md.bold(city_name)), parse_mode=ParseMode.MARKDOWN
        )

        try:
            r = requests.get(
                f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={open_weather_token}&units=metric'
            )
            data = r.json()
            true_city = data['city']['name']
            await callback.message.answer(f'Погода в городе: {true_city}')
            
            counter = 0
            for i in data['list']:
                date = data['list'][counter]['dt_txt']
                temp = round(data['list'][counter]['main']['temp'])
                weather_description = data['list'][counter]['weather'][0]['main']
                if weather_description in code_to_smile:
                    weather = code_to_smile[weather_description]
                else:
                    weather = 'что-то неопределенное'

                humidity = data['list'][counter]['main']['humidity']
                pressure = round(data['list'][counter]['main']['pressure']*0.750063755419211)
                wind = round(data['list'][counter]['wind']['speed'], 1)

                if data['list'][counter]['dt_txt'][11:13] == '12':
                    await callback.message.answer(f'Дата: {date}\nТемпература: {temp} C°\nНа улице: {weather}\n'
                                f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
                                )
                    counter += 1
                else:
                    counter += 1
                    continue

            #await callback.answer(show_alert=False)
                        

        except:
            await callback.answer('Проверьте название города', show_alert=True)     
    


    else:
        await callback.answer('обратитесь к администратору', show_alert=True)   


