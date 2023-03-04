from aiogram import types
from create_bot import dp, bot
import json, string, random
from keyboards.kb_ordinary import kboard
import os

lst = ['Лучше воздержаться от мата', 'Господа, ну право, что за выражения!', 'Ну что вы опять, хорошо же общались', 
        'Вызываю пояснительную бригаду', 'Господи помилуй', 'Расшифруйте, пожалуйста', 'Что значит это новомодное словечко?']

#@dp.message_handler()
# async def cmd_cenz(message : types.Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
#         .intersection(set(json.load(open('cenz.json')))) != set():
#         await message.reply(random.choice(lst))


#@dp.message_handler()
async def welcome(message : types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Нажми /start')
    elif {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply(random.choice(lst))


#@dp.message_handler(commands='start') то же самое, что #@dp.message_handler(commands=['start', 'help'])
#@dp.message_handler(Text(equals='start', ignore_case=True))
async def cmd_start(message : types.Message):
    # picture = open('pic/sticker.webp', 'r')
    # file = open(os.path.dirname(os.path.abspath(__file__))
    #             + '/pic/sticker.webp', 'rb')
    # await message.answer(file)
    await message.reply('Дратути', reply_markup=kboard)



