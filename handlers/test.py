from aiogram import types
from create_bot import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inButton1 = InlineKeyboardButton(text='Нажми меня', callback_data='www')
inkb = InlineKeyboardMarkup(row_width=1).add(inButton1)


# @dp.message_handler(Text(equals='Тест'))
async def cmd_test(message : types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inkb)
    
@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
    await callback.message.answer('Нажато')
    await callback.answer('Готово', show_alert=True)
