import requests
import json
import pprint

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
heroes = response.json()

with open('superherofile.json', "w") as f:
    json.dump(heroes, f)