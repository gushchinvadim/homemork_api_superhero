# ДЗ по API
## 1. superhero_1
- Создаем словарь the_smartest_superhero с ключами героями, значения пустые;
- Перебираем циклом всех героев;
- Объявляем переменную name и записываем в нее словарь из ключей имен, с пустыми значениями;
- Проверяем есть ли имена полученные из json в совареthe_smartest_superhero;
- Получаем для выбранных имен intelligence из json;
- Выбираем максимальное значениеintelligence и получаем ключ!!!
## 2. superhero_2


## 3. translater
- Согласно документации Яндекса получаем API ключ и проверяем обязательные параметры для запроса;
- URL оборачиваем в функцию f для того чтобы внести переменные {token} и {word};
- Далее проходим циклами до: 
- for el in data['def']: 
- for i in el['tr']:
- trans_words.append(i['text'])
### ИЛИ
- Но можно было и вот так:     
- response = requests.get(url=url, params=param).json()
- trans_word = response['def'][0]['tr'][0]['text']