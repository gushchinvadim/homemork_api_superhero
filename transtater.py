import requests
def translate_word(word):
    trans_words = []
    token = 'dict.1.1.20250112T083017Z.1a7753b1f249dd3c.3a59736e51a0b96543ebb7315b0cf86e2f1f7e84'
    url = f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={token}&lang=ru-en&text={word}'
    response = requests.get(url)
    data = response.json()
    # print(data)
    for el in data['def']:
        for i in el['tr']:
            trans_words.append(i['text'])
    trans_word = trans_words[0]
    print(trans_word)

    return trans_word

if __name__ == '__main__':
    word = 'стол'
    assert translate_word(word) == 'table'
