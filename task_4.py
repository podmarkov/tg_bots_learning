import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN =



updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={-1}').json()


print(updates)

print(updates['result'][0]['message']['text'])