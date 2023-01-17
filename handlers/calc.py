from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboards.kb_inline import inkb
from operators import operator


class Form(StatesGroup):
    number1 = State()
    number2 = State()

lst = [1, 2, 3, 4]


# @dp.message_handler(Text(equals='Калькулятор'))
async def cmd_calc(message : types.Message):
    await Form.number1.set()
    await message.answer('Введите 1 число')


@dp.message_handler(state=Form.number1)
async def load_number1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number1'] = int(message.text)
        global a
        a = data['number1']
    await Form.next()
    await message.answer('Введите 2 число')

@dp.message_handler(state=Form.number2)
async def load_number1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number2'] = int(message.text)
        global b
        b = data['number2']
    await state.finish()
    await bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='condition_'))
async def button_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    try:
        if res in lst:
                if res == 1:
                    operator.summ(a, b)
                    await callback.message.answer(operator.c)
                elif res == 2:
                    operator.min(a, b)
                    await callback.message.answer(operator.c)
                elif res == 3:
                    operator.mult(a, b)
                    await callback.message.answer(operator.c)
                elif res == 4:
                    operator.div(a, b)
                    await callback.message.answer(operator.c)
            
        else:
            await callback.answer('обратитесь к администратору', show_alert=True)


    except:
        await callback.answer('что-то пошло не так')
