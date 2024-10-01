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

@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра',
                                'играть', 'хочу играть']))
async def start_game(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret'] = secret_number()
        user['games'] += 1
        await message.answer(f'''Игра началась! Количество попыток: {user["attempts"]}''')
    else:
        await message.answer(f'''Игра уже идет. 
Вы можете:
Прислать число от 1 до 100
Или ввести /stat для просмотра статистики
или /cancel для прерывания игры
''')

@dp.message(F.text.lower().in_(['нет', 'не хочу', 'в другой раз']))
async def not_game(message: Message):
    if not user['in_game']:
        await message.answer(f'''Жаль, как захотите играть, приходите''')
    else:
        await message.answer(f'''Мы же уже играем, пришлите число от 1 до 100''')

@dp.message(F.text.isdigit())
async def guess_number(message: Message):
    if user['in_game']:
        guess = int(message.text)
        if guess in range(1, 101):
            if guess == user['secret']:
                user['won'] += 1
                await message.answer(f'Вы угадали! Загаданное число: {user["secret"]}')
            elif guess < user['secret']:
                await message.answer(f'Вы ввели число меньше загаданного. Осталось попыток: {user["attempts"] - 1}')
                user['attempts'] -= 1
            else:
                await message.answer(f'Вы ввели число больше загаданного. Осталось попыток: {user["attempts"] - 1}')
                user['attempts'] -= 1
        else:
            await message.answer(f'Введите число от 1 до 100')


