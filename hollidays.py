import requests
import time

sity_list = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']

# _coordinates = [
#     ('55.7514952', '37.618153095505875'),
#     ('52.3727598', '4.8936041'),
#     ('53.4071991', '-2.99168')
# ]
# for coord in _coordinates:
#     lat, lon = coord[0], coord[1]
# url = "https://geocode.maps.co/reverse"
# api_key = '67839b9207d1c680106760ajuccbbe3'
# param = {
#     'lat': lat,
#     'lon': lon,
#     'key': api_key
# }
# response = requests.get(url=url, params=param).json()
# city = response['address']['city']
# if city in sity_list:
#     print(city)
# else:
#     time.sleep(10)
#          continue



# def find_uk_city(coordinates:list) -> str:
#     """Ваш код здесь"""
#     ...
#
#
# if __name__ == '__main__':
#     _coordinates = [
#         ('55.7514952', '37.618153095505875'),
#         ('52.3727598', '4.8936041'),
#         ('53.4071991', '-2.99168')
#     ]
#     assert find_uk_city(_coordinates) == 'Liverpool'
sity_dict = {}
api_key = '67839b9207d1c680106760ajuccbbe3'

for adress in sity_list:
    pass
    url = 'https://geocode.maps.co/search'
    param = {
        'q': adress,
        'key': api_key

    }
    response = requests.get(url=url, params=param).json()
    coord_dict = response[0]
    coord = coord_dict['lat'], coord_dict['lon']

    print(adress, coord)


# url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={api_key}'
# longitude = -2.99168
# url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={api_key}'
# payload = {}
# headers = {}