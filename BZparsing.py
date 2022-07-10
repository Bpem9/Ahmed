import requests
import os
from bs4 import BeautifulSoup
import json
from pprint import pprint
import re
import psycopg2
from config import *
from dotenv import load_dotenv

def id_from_database():
    load_dotenv()
    connection = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode='require')
    connection.autocommit = True
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT flat_id
            FROM flats
            ''')
            id_list = [apt[0] for apt in cursor.fetchall()]
        return id_list
    except Exception as e:
        print(f'[SQL-INFO] Error while working with database: *{e}*')
    finally:
        connection.close()
        print('[SQL-INFO] Database connection successfully closed')
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
            'Ссылка':SITE + apt.find('a').get('href')
        }
    with open('apts_list.json', 'w+') as file:
        json.dump(apts, file, indent=4, ensure_ascii=False)
def checking_for_new_apts(html, id_list):
    with open('apts_list.json', 'r', encoding='windows-1251') as file:
        old_apts = json.loads(file.read())
    soup = BeautifulSoup(html.text, 'lxml')
    apts_info = soup.find_all('li', class_='announcement-container')
    new_apts = {}
    for apt in apts_info:
        new_apt_id = re.sub(ID_REG, '\\1', apt.find('a').get('href'))
        if int(new_apt_id) not in id_list:
            # collecting in variables necessary information (id, type, location, price, link)
            type_of_house = re.sub(HOUSE_TYPE_REG, '\\2', apt.find('a').get('content'))
            house_location = apt.find_next('meta', attrs={'itemprop': 'areaServed'}).get('content')
            price_of_house = apt.find_next('meta', attrs={'itemprop': 'price'}).get('content')
            link = SITE + apt.find('a').get('href')
            # creating a new apts list for messaging to telegram and adding new ones to exsisting apts list
            old_apts[new_apt_id] = new_apts[new_apt_id] = {
                'Тип': type_of_house,
                'Локация': house_location,
                'Цена': price_of_house,
                'Ссылка': link
            }
        else:
            continue
    # print(new_apts)
    with open('apts_list.json', 'r+', encoding='windows-1251') as file:
        json.dump(old_apts, file, indent=4, ensure_ascii=False)
    # print(new_apts)
    return new_apts
def adding_to_database(dict, list):
    load_dotenv()
    connection = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode='require')
    connection.autocommit = True
    try:
        with connection.cursor() as cursor:
            i = 1
            for key, value in dict.items():
                cursor.execute('''
                INSERT INTO flats(pk_flat_id, flat_id, price, address, fl_type, link)
                VALUES (%s, %s, %s,  %s,  %s,  %s)
                ''', ((len(list) + i), key, value['Цена'], value['Локация'], value['Тип'], value['Ссылка'])
                )
                i += 1
    except Exception as e:
        print(f'[SQL-INFO] Error while adding to database: *{e}*')
    finally:
        connection.close()
        print('[SQL-INFO] Database connection successfully closed')


if __name__ == '__main__':
    html = get_content(URL)
    #get_info(html) # - first time collecting information: creating an 'old_apts' list
    id_list = id_from_database()
    print(id_list)
    adding_to_database(checking_for_new_apts(html, id_list), id_list)
