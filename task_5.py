import requests
import time

from random import choice
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7306454882:AAG-PS2hldOdkk3TWgnzRDDsjvDxUakCeKs'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
API_FOXES_URL = 'https://randomfox.ca/floof/'
api_urls = (API_CATS_URL, API_DOGS_URL, API_FOXES_URL)
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str


while counter < 100:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    #print(updates)

    if updates['result']:
        offset = updates['result'][0]['update_id']
        chat_id = updates['result'][0]['message']['from']['id']
        pet_url = choice(api_urls)
        pet_response = requests.get(pet_url)
        if pet_response.status_code == 200:
            pet_link = eval('pet_response.json()' + {API_CATS_URL: "[0]['url']",
                                                     API_DOGS_URL: "['url']",
                                                     API_FOXES_URL: "['image']"}[pet_url])
            requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={pet_link}')
        else:
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')




    time.sleep(1)
    counter += 1
