import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-peugeot/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
    'accept':'*/*'
}
HOST = 'https://auto.ria.com'

def get_html(url, params=None):
#   Возвращает Http-ответ
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def souping_html(html):
#   Вытаскивает из http-ответа нужную инфу
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('section', class_='proposition')
    cars = [{
        'title':item.find('span', class_='link').get_text(strip=None),
        'link':HOST + item.find('a').get('href')
    } for item in items]
    print(cars[0])

def parse():
#   Выводит на экран
    html = get_html(URL)
    souping_html(html.text)

parse()