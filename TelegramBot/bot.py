
import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
logFilePath = os.getenv('logFilePath')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    name = message.from_user.username
    await message.answer(f"Hello {name}!")

@dp.message(F.text == 'temperature')
async def temprt(message: Message):
    data = open(logFilePath, 'r')
    logs = data.read()
    await message.answer(str(logs))

@dp.message(F.text == 'test')
async def temprt(message: Message):
    await message.answer("ok!")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
