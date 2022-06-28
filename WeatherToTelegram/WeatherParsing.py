import json
import requests
from bs4 import BeautifulSoup
from config import open_api_token
from pprint import pprint
import aiogram

URL ='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
weather_description = {
    'Clear':'Ясно \U00002600',
    'Clouds':'Облачно \U00002601',
    'Rain':'Дождь \U0001F327',
    'Drizzle':'Моросит \U0001F326',
    'Thunderstorm':'Гроза \U000026C8',
    'Mist':'Туман \U0001F32B',
    'Snow':'Снег \U0001F328'
}

def get_weather(city, open_api_token):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_api_token}&units=metric')
        data = r.json()
        city_id = data["name"]
        temperature = data['main']['temp']
        weather = data['weather'][0]['main']
        if weather in weather_description:
            wd = weather_description[weather]
        else:
            wd = 'Посмотри в окно, непонятно'
        return(f'Город : {city_id}\nТемпература : {temperature}C°\nПогода : {wd}')

    except:
        return('Ошибка')

def main():
    city = input('Введите город: ')
    get_weather(city, open_api_token)


if __name__ == '__main__':
    main()