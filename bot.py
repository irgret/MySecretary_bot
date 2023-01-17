from aiogram import executor
from create_bot import dp
from handlers import controller


async def on_startup(_):
    print('Бот онлайн')



controller.controller(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




# 3 метода ответа:
# await message.answer(message.text)  не цитирует, отвечает в общем чате
# await message.reply(message.text)    цитирует сообщение в общем чате
# await bot.send_message(message.from_user.id, message.text)  не цитирует сообщение и отвечает в личку


#@dp.message_handler(commands=['start', 'help'])
# async def cmd_start(message : types.Message):
    # await message.reply('Дратути', reply_markup=kboard)
    #await bot.send_message(message.from_user.id, 'Тут как тут', reply_markup=kboard)
    # try:
    #     await bot.send_message(message.from_user.id, 'Тут как тут', reply_markup=kboard)
    #     # await message.delete()
    # except:
    #     await message.reply('Что-то пошло не так...')