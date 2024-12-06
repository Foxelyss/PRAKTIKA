import json
import requests
from datetime import datetime

API_key = '***REMOVED***'

current_date = datetime.now().date()


def weather_city(location):
    weathers = load_history()

    for x in weathers:
        if x["date"] == str(current_date) and x["name"] == location:
            return x

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': API_key,
        'q': location,
        'units': 'metric',
        'lang': 'ru'}
    response = requests.get(base_url, params=params)
    data = response.json()

    save = data
    save["date"] = str(datetime.now().date())

    weathers.append(save)

    with open("weather_history.json", "w", encoding='utf8') as file:
        json.dump(weathers, file, indent=2, ensure_ascii=False)

    return data


def load_history():
    try:
        with open("weather_history.json", "r", encoding='utf8') as file:
            return json.load(file)
    except:
        return []


def get_default_city():
    history = load_history()
    if len(history) > 0:
        if "name" in history[-1]:
            return history[-1]["name"]

    return "Томск"


print('Введите город или Enter(если вы вводили прошлый раз город, то он будет по умолчанию)')

city = input().lower()
if len(city) < 1:
    city = get_default_city()

data = weather_city(city)

print("Погода на сегодня в", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Как ощущается температура:", data['main']['feels_like'])
print("Температура минимальная:", data['main']['temp_min'])
print("Температура максимальная:", data['main']['temp_max'])
print("Видимость (м):", data['visibility'])
print("Скорость ветра (м/с):", data['wind']['speed'])
