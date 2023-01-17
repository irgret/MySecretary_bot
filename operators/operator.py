from aiogram import types
from create_bot import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.kb_inline import inkb
from aiogram.dispatcher.filters import Text


c = 0

def summ(a, b):
    global c
    c = a + b
    return c

def min(a, b):
    global c
    c = a - b
    return c

def mult(a, b):
    global c
    c = a * b
    return c

def div(a, b):
    global c
    c = round(a/b, 2)
    return c


           