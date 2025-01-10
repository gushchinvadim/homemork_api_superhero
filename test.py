import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
heroes = response.json()
print(heroes)

def get_the_smartest_superhero(superheros):
     dict_heroes = {}
     the_smartest_superhero = ''
     for id in superheros:
        for hero in heroes:
            if hero['id'] == id:
               dict_heroes['name'] = hero['powerstats']['intelligence']
            the_smartest_superhero = max(dict_heroes)
     return the_smartest_superhero

if __name__ == '__main__':
#     assert get_the_smartest_superhero([332, 149, 655]) == 'Thanos'
print(get_the_smartest_superhero([332, 149, 655]))