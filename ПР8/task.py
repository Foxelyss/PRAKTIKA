import json
import requests
from datetime import datetime

API_key = '***REMOVED***'

current_date = datetime.now().date()

def weather_city(lat_lon):
    weathers = load_history()

    for x in weathers:
        if x["date"] == str(current_date):
            return x

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': API_key,
        'lat': lat_lon[0],
        'lon': lat_lon[1],
        'units': 'metric',
        'lang': 'ru'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data


def location_lat_lon_city(city):
    try:
        with open("city_lat_lon.json", "r", encoding='utf8') as file:
            meanings = json.load(file)
    except:
        meanings = []

    for i in range(len(meanings)):
        if meanings[i]['name'] == city:
            return tuple(meanings[i]['lat_lon'])

    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_key}').json()

    lat = response[0]['lat']
    lon = response[0]['lon']
    json_dump = {"name": city, "lat_lon": [lat, lon]}
    meanings.append(json_dump)

    with open("city_lat_lon.json", "w", encoding='utf8') as file:
        json.dump(meanings, file, indent=4, ensure_ascii=False)
    return lat, lon


def load_history():
    try:
        with open("weather_history.json", "r", encoding='utf8') as file:
            return json.load(file)
    except:
        return []


history = load_history()
print('Введите город или Enter(если вы вводили прошлый раз город, то он будет по умолчанию)')
city = input().capitalize()
if len(city) < 1:
    city = history[-1]["default"]
lat_lon = location_lat_lon_city(city)
mean = weather_city(lat_lon)

print("Погода на сегодня в", city)
print("Погодные условия:", mean['weather'][0]['description'])
print("Температура:", mean['main']['temp'])
print("Как ощущается температура:", mean['main']['feels_like'])
print("Температура минимальная:", mean['main']['temp_min'])
print("Температура максимальная:", mean['main']['temp_max'])
print("Видимость (м):", mean['visibility'])
print("Скорость ветра (м/с):", mean['wind']['speed'])

if history[-1]["date"] != str(current_date):
    save = mean
    save["date"]: str(datetime.now().date())
    save["default"]: city

    history.append(save)
    with open("weather_history.json", "w", encoding='utf8') as file:
        json.dump(history, file, indent=2, ensure_ascii=False)
