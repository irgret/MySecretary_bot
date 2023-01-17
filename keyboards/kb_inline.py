from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inButton1 = InlineKeyboardButton(text='Сложение [+]', callback_data='condition_1')
inButton2 = InlineKeyboardButton(text='Вычитание [-]', callback_data='condition_2')
inButton3 = InlineKeyboardButton(text='Умножение [*]', callback_data='condition_3')
inButton4 = InlineKeyboardButton(text='Деление [/]', callback_data='condition_4')
inButton5 = InlineKeyboardButton(text='test 5', callback_data='condition_5')
inButton6 = InlineKeyboardButton(text='test 6', callback_data='condition_6')

inkb = InlineKeyboardMarkup(row_width=2).add(inButton1, inButton2, inButton3, inButton4, inButton5, inButton6)