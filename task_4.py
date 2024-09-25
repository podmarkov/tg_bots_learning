import requests


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7306454882:AAG-PS2hldOdkk3TWgnzRDDsjvDxUakCeKs'



updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={-1}').json()  #.json()


print(updates)

#print(updates['result'][0]['message']['text'])