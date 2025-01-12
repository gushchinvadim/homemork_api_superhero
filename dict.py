import requests
# import json
# import pprint
#
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# response = requests.get(url)
# heroes = response.json()
#
# with open('superherofile.json', "w") as f:
#     json.dump(heroes, f)
#
#     dct = {'a': 1, 'b': 2}
#     lst1 = ['c', 'd']
#     lst2 = [3, 4]
#     for i in range(0, 2):
#
#         key = lst1[i]
#         value = lst2[i]
#         dct[key] = value
#     print(dct)

# url = "https://httpbin.org/get"
# resp = requests.get(url)
# print(resp.json())

r = requests.get("https://netology.ru/")
print(r)