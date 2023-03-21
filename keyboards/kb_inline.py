from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inButton1 = InlineKeyboardButton(text='Сложение [+]', callback_data='condition_1')
inButton2 = InlineKeyboardButton(text='Вычитание [-]', callback_data='condition_2')
inButton3 = InlineKeyboardButton(text='Умножение [*]', callback_data='condition_3')
inButton4 = InlineKeyboardButton(text='Деление [/]', callback_data='condition_4')
inButton5 = InlineKeyboardButton(text='test 5', callback_data='condition_5')
inButton6 = InlineKeyboardButton(text='test 6', callback_data='condition_6')

inkb = InlineKeyboardMarkup(row_width=2).add(inButton1, inButton2, inButton3, inButton4, inButton5, inButton6)

inButton_weather_1 = InlineKeyboardButton(text='Погода на сегодня', callback_data='weather_today')
inButton_weather_2 = InlineKeyboardButton(text='Прогноз на 5 дней', callback_data='weather_forecast')
inkb_weather = InlineKeyboardMarkup(row_width=2).add(inButton_weather_1, inButton_weather_2)