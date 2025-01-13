
import requests
import time
def find_uk_city(coordinates:list) -> str:
   sity_list = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
   API_KEY = '67839b9207d1c680106760ajuccbbe3'
   for lat, lon in coordinates:
       time.sleep(2)
       response = requests.get(f'https://geocode.maps.co/reverse?lat={lat}&lon={lon}&api_key={API_KEY}')
       data = response.json()
       city = data['address']['city']
       if city in sity_list:
          return city
if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'


# sity_dict = {}
# api_key = '67839b9207d1c680106760ajuccbbe3'
#
# for adress in sity_list:
#     pass
#     url = 'https://geocode.maps.co/search'
#     param = {
#         'q': adress,
#         'key': api_key
#
#     }
#     response = requests.get(url=url, params=param).json()
#     coord_dict = response[0]
#     coord = coord_dict['lat'], coord_dict['lon']
#
#     print(adress, coord)


# url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={api_key}'
# longitude = -2.99168
# url = f'https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={api_key}'
# payload = {}
# headers = {}