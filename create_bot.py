from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

bot = Bot(token=os.getenv('TOKEN'))
# proxy_url = 'http://proxy.server:3128'
# bot = Bot(token=TOKEN, proxy=proxy_url)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
