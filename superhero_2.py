import requests

def get_the_smartest_superhero(superheros):
    the_smartest_superhero = {}
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    heroes = response.json()
    for hero in heroes:
        for x in superheros:
            if x == hero['id']:
             the_smartest_superhero.update({hero['name']: hero['powerstats']['intelligence']})
    get_the_smartest_superhero = max (the_smartest_superhero, key = the_smartest_superhero.get)
    return get_the_smartest_superhero

if __name__ == '__main__':
    print(get_the_smartest_superhero)

