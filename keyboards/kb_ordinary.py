from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Узнать погоду')
b2 = KeyboardButton('Курс валют')
b3 = KeyboardButton('Тест')
b4 = KeyboardButton('Калькулятор')

kboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kboard.row(b1, b2).add(b3).insert(b4)
# kboard.row(b1, b2).add(b3).add(b4).insert(b5)




# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить локацию', request_location=True)
