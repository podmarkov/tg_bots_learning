from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from random import randint
import my_token

BOT_TOKEN = my_token.tkn1
attempts = 5
user = {'in_game': False,
        'secret': None,
        'games': 0,
        'won': 0,
        'lost': 0,
        'attempts': attempts}
def secret_number():
    return randint(1, 100)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(f'''Привет! Этот бот играет в угадай число
Чтобы узнать подробные правила, пиши /help''')

# Этот хэндлер будет срабатывать на команду "/help"

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        f'''Игра в угадай число. Тебе дается 5 попыток, чтобы угадать загаданное число.
Чтобы начать игру, введи "Да", "Давай", "Сыграем",
Не согласиться - введи "Нет", "Не хочу", "В другой раз",
Команда /stat покажет статистику попыток
Команда /cancel прерывает игру
Сыграем?
''')

@dp.message(Command(commands=['stat']))
async def show_stats(message: Message):
    await message.answer(
        f'''Побед: {user['won']}, 
поражений: {user['lost']}, 
попыток: {user['games']}
''')


@dp.message(Command(commands=['cancel']))
async def stop(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer(f'''Игра прервана''')

