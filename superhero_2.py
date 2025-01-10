import requests
import json
import pprint

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
heroes = response.json()
# print(heroes)
for hero in heroes: #Вытащили все словари из списка
    intelligence = hero['powerstats']['intelligence']


    x = {}

    print(hero['id'], hero['name'], intelligence)



