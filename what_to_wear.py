# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:54:50 2022

@author: dedaster
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import keyboard

url = 'https://www.foreca.ru/Russia/Saint_Petersburg'
headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
t_str = soup.find("span", attrs={"class": "txt-xxlarge"}).find('strong').text
t_s_f = soup.find("div", attrs={"class": "c1"}).find('div', attrs={'class': 'right'}).find('strong').text
t = int(t_str)
t_feel = int(t_s_f.replace('°', ''))

def clothes():
    
    temp_min = (skin['МинТемп'] <= t)
    temp_max = (skin['МаксТемп'] >= t)
    temp = skin.loc[temp_min & temp_max]
    
    top = temp[temp['Часть'].isin(['верх'])].sample(n=1)
    over = temp[temp['Часть'].isin(['поверх'])].sample(n=1)
    bottom = temp[temp['Часть'].isin(['низ'])].sample(n=1)
    socks = temp[temp['Часть'].isin(['носки'])].sample(n=1)
    
    result = pd.concat([top, over, bottom, socks], ignore_index=True)

    print()
    print(result.iloc[:, 2:3])
    print()

    
while True:
    skin = pd.read_csv('\Git\what_to_wear\what_to_wear.csv', \
                       names = ['Часть', 'Цвет', 'Название', 'МинТемп', 'МаксТемп'])
    print()
    if t > 0:
        print("Сейчас +", t)
        print("Ощущается как", t_feel)
    else:
        print("Сейчас", t)
        print("Ощущается как", t_feel)
    clothes()
    print('или')
    clothes()
    
    print('Чтобы перезапустить нажми Enter')

    for i in range(11):     
        print()
        
    keyboard.wait('enter')


    
