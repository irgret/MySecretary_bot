from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from handlers import weather, exchange, calc, test, start




def controller(dp : Dispatcher):
    dp.register_message_handler(start.cmd_start, commands=['start', 'help', 'bot'])
    dp.register_message_handler(start.cmd_start, Text(equals=['бот', 'мистер бот', 'bot'], ignore_case=True))
    dp.register_message_handler(test.cmd_test, Text(equals='Тест'))
    dp.register_message_handler(weather.cmd_weather, Text(equals='Узнать погоду', ignore_case=True))
    dp.register_message_handler(exchange.cmd_rate, Text(equals=['Курс валют', 'курс валюты'], ignore_case=True))
    dp.register_message_handler(calc.cmd_calc, Text(equals='Калькулятор', ignore_case=True))
    dp.register_message_handler(start.welcome)







    # dp.register_message_handler(start.cmd_start, commands=['start', 'help', 'bot'])
    # dp.register_message_handler(test.cmd_test, commands=['Тест'])
    # dp.register_message_handler(weather.cmd_weather, commands=['Узнать_погоду'])
    # dp.register_message_handler(exchange.cmd_rate, commands=['Курс_валют'])
    # dp.register_message_handler(calc.cmd_calc, commands=['Калькулятор'])