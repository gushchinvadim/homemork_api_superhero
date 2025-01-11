from tkinter.font import names

import requests


def get_the_smartest_superhero() -> str:
    the_smartest_superhero = {'Hulk' : 0, 'Captain America' : 0, 'Thanos' : 0}
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    for hero in response.json():
      name = hero.get('name', '')
      if name in the_smartest_superhero:
        the_smartest_superhero[name] = hero.get('powerstats'). get('intelligence')
    x = max(the_smartest_superhero, key=the_smartest_superhero.get)
    return x
if __name__ == '__main__':
  print(get_the_smartest_superhero())
