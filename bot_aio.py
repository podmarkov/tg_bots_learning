from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import my_token

BOT_TOKEN = my_token.tkn1

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(f'''Привет! Этот бот шлёт тебе фоточки животных''')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        f'''Выбери команду из меню
и я отправлю тебе 
фото выбранного животного'''
    )

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=f'Фигу тебе, а не {message.text}')


if __name__ == '__main__':
    dp.run_polling(bot)