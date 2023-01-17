from datetime import date
import requests
from aiogram import types


# @dp.message_handler(Text(equals='Курс валют'))
async def cmd_rate(message : types.Message):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    name_USD = data['Valute']['USD']['Name']
    value_USD = round(data['Valute']['USD']['Value'], 2)
    nominal_USD = data['Valute']['USD']['Nominal']

    name_EUR = data['Valute']['EUR']['Name']
    value_EUR = round(data['Valute']['EUR']['Value'], 2)
    nominal_EUR = data['Valute']['EUR']['Nominal']

    name_TJS = data['Valute']['TJS']['Name']
    value_TJS = round(data['Valute']['TJS']['Value'], 2)
    nominal_TJS = data['Valute']['TJS']['Nominal']

    await message.answer(f'Курс ЦБ к рублю на {date.today()}\n'
                         f'{nominal_USD} {name_USD}: {value_USD}\n'
                         f'{nominal_EUR} {name_EUR}: {value_EUR}\n'
                         f'{nominal_TJS} {name_TJS}: {value_TJS}')

