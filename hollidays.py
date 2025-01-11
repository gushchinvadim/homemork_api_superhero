import requests
import time


def find_uk_city(coordinates: list) -> str:
    API = '65ae97b123696043220487avude3e26'
    URL = 'https://geocode.maps.co/reverse?'

    uk_city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']

    for lat, lon in coordinates:
        response = requests.get(f'{URL}lat={lat}&lon={lon}&key={API}')
        data = response.json()
        city = data.get('address', {}).get('city')

        if city in uk_city:
            return city
        else:
            time.sleep(15)
            continue


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'