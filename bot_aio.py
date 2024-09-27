from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import requests

import my_token

BOT_TOKEN = my_token.tkn1
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
API_FOXES_URL = 'https://randomfox.ca/floof/'
API_CAPY_URL = 'https://api.capy.lol/v1/capybara?json=true'
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

# Этот хэндлер будет срабатывать на команду "/cat"
@dp.message(Command(commands=['cat']))
async def send_cat(message: Message):
    await message.answer_photo(photo=f'{requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]}'
    )

# Этот хэндлер будет срабатывать на команду "/dog"
@dp.message(Command(commands=['dog']))
async def send_dog(message: Message):
    await message.answer_photo(photo=f'{requests.get("https://random.dog/woof.json").json()["url"]}'
    )


# Этот хэндлер будет срабатывать на команду "/fox"
@dp.message(Command(commands=['fox']))
async def send_fox(message: Message):
    await message.answer_photo(photo=f'{requests.get("https://randomfox.ca/floof/").json()["image"]}'
    )

# Этот хэндлер будет срабатывать на команду "/capybara"
@dp.message(Command(commands=['capybara']))
async def send_capybara(message: Message):
    await message.answer_photo(photo=f'{requests.get("https://api.capy.lol/v1/capybara?json=true").json()["data"]["url"]}'
    )

# Этот хэндлер будет сра��атывать на любые ваши фотографии
@dp.message(F.photo)
async def echo_photo(message: Message):
    await message.reply_photo(photo=message.photo[0].file_id)

@dp.message(F.video)
async def echo_video(message: Message):
    await message.reply_video(video=message.video.file_id)

@dp.message(F.audio)
async def echo_audio(message: Message):
    await message.reply_audio(audio=message.audio.file_id)

@dp.message(F.voice)
async def echo_voice(message: Message):
    await message.reply_voice(voice=message.voice.file_id)

@dp.message(F.sticker)
async def echo_sticker(message: Message):
    await message.reply_sticker(sticker=message.sticker.file_id)

@dp.message(F.document)
async def echo_document(message: Message):
    await message.reply_document(document=message.document.file_id)

@dp.message(F.animation)
async def echo_animation(message: Message):
    await message.reply_animation(animation=message.animation.file_id)



# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)