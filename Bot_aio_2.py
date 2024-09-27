from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import requests

import my_token

BOT_TOKEN = my_token.tkn1


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(f'''Привет! Это эхо бот''')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        f'''Напиши любое сообщение, и я отправлю его тебе обратно'''
    )

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='''Данный тип апдейтов не поддерживается
методом send_copy''')


if __name__ == '__main__':
    dp.run_polling(bot)