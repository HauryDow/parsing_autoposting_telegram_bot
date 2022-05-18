#!/usr/bin/python3

import telegram
import time
import requests
from bs4 import BeautifulSoup

TOKEN = 'some_token'
bot = telegram.Bot(token=TOKEN)
chat_id='some_id'
url='https://select.by/kursy-valyut'

response=requests.get(url)
soup=BeautifulSoup(response.text, 'lxml')#'html.parser', 'lxml'
data=soup.find_all('div', class_='col h2')
l=[]
for i in data:
    l.append(i.text)
post=f'💵💶Лепшыя курсы валют на сёння: \n \n' \
     f'USD 🇺🇸 : купля {l[0]}, продаж {l[1]}; \n' \
     f'EUR 🇪🇺 : купля {l[2]}, продаж {l[3]};\n' \
     f'RUB 🇷🇺: купля {l[3]}, продаж {l[4]}.'

bot.send_message(chat_id, post)

time.sleep(86400)
