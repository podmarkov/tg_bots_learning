import requests
import my_token

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = my_token.tkn()



updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={-1}').json()  #.json()


print(updates)

#print(updates['result'][0]['message']['text'])