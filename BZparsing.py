import requests
from bs4 import BeautifulSoup
import json
import pprint
import re


pp = pprint.PrettyPrinter()
URL = 'https://***/real-estate/houses-and-villas-rent/lemesos-district-limassol/?type_view=line&ordering=newest&price_max=1500'
HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
    'accept':'*/*'
}
ID_REG = r'/adv/([0-9]{7})(\_)(.*)'
HOUSE_TYPE_REG = r'(\s?)(.*)(\s)to rent$'
HOST = 'https://***'


def get_content(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS)
    return r
def get_info(html):
    soup = BeautifulSoup(html.text, 'lxml')
    apts_info = soup.find_all('li', class_='announcement-container')
    apts={}
    for apt in apts_info:
        apts[re.sub(ID_REG, '\\1', apt.find('a').get('href'))] = {
            'Тип':re.sub(HOUSE_TYPE_REG,'\\2', apt.find('a').get('content')),
            'Локация' : apt.find_next('meta', attrs={'itemprop': 'areaServed'}).get('content'),
            'Цена' : apt.find_next('meta', attrs = {'itemprop':'price'}).get('content'),
            'Ссылка':HOST + apt.find('a').get('href')
        }
    with open('apts_list.json', 'w+') as file:
        json.dump(apts, file, indent=4, ensure_ascii=False)

def checking_for_new_apts(html):
    with open('apts_list.json', 'r', encoding='windows-1251') as file:
        old_apts = json.loads(file.read())

    soup = BeautifulSoup(html.text, 'lxml')
    apts_info = soup.find_all('li', class_='announcement-container')
    new_apts = {}
    for apt in apts_info:
        new_apt_id = re.sub(ID_REG, '\\1', apt.find('a').get('href'))
        if new_apt_id in old_apts:
            continue
        else:
            type_of_house = re.sub(HOUSE_TYPE_REG, '\\2', apt.find('a').get('content'))
            house_location = apt.find_next('meta', attrs={'itemprop': 'areaServed'}).get('content')
            price_of_house = apt.find_next('meta', attrs={'itemprop': 'price'}).get('content')
            link = HOST + apt.find('a').get('href')

            new_apts[re.sub(ID_REG, '\\1', apt.find('a').get('href'))] = {
                'Тип': type_of_house,
                'Локация': house_location,
                'Цена': price_of_house,
                'Ссылка': link
            }
            old_apts[re.sub(ID_REG, '\\1', apt.find('a').get('href'))] = {
                'Тип': type_of_house,
                'Локация': house_location,
                'Цена': price_of_house,
                'Ссылка': link
            }

    with open('apts_list.json', 'r+', encoding='windows-1251') as file:
        json.dump(old_apts, file, indent=4, ensure_ascii=False)

#   for new_apt in new_apts:
    return new_apts
#   return f"Тип - {type_of_house},\nЛокация - {house_location},\nЦена - {price_of_house},\nСсылка - {link}"

if __name__ == '__main__':
    html = get_content(URL)
    #get_info(html)
    checking_for_new_apts(html)