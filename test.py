# # import requests
# #
# #
# #
# # url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# # response = requests.get(url)
# # heroes = response.json()
# # def get_the_smartest_superhero(superheros):
# #     dict_heroes = {}
# #     the_smartest_superhero = ''
# #     for id in superheros:
# #         for hero in heroes:
# #             if hero['id'] == id:
# #                 dict_heroes[hero['name']] = hero['powerstats']['intelligence']
# #                 the_smartest_superhero = max(dict_heroes)
# #     return the_smartest_superhero
# #
# # get_the_smartest_superhero([332, 149, 655])
#
# d = {10: 100, 81:500, 3:2000}
# s=max(d,key=d.get)
# print(s)
import requests
import json

# def get_the_smartest_superhero() -> str:
the_smartest_superhero = {}
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
# heroes = response.json()

for hero in response.json(): #Вытащили все словари из списка
    # intelligence = hero['powerstats']['intelligence']
    id_dict = [
            hero['id'],
            hero['name'],
            hero['powerstats']['intelligence']
    ]
    # print(id_dict)
    superheros = [200,300,400]
    for x in superheros:
        if x == hero['id']:
         the_smartest_superhero.update({hero['name']: hero['powerstats']['intelligence']})
print(the_smartest_superhero)
get_the_smartest_superhero = max (the_smartest_superhero, key = the_smartest_superhero.get)
print(get_the_smartest_superhero)




    #print(hero['id'], hero['name'], intelligence)



