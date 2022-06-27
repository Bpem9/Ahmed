# -*- coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

URL = '****'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
    'accept': '*/*'
}

def get_content(url, params=None):
    r = requests.get(url=url, headers=HEADERS, params=params)
    soup = BeautifulSoup(r.text, 'lxml')
    articles = soup.find_all('a', class_='article-card')
    cards, fresh_news = carding(articles)
    jsoning(cards)


def carding(arti):
    with open('news_archive.json', 'r+', encoding='windows-1251') as file:
        cards = json.load(file)
    fresh_news = {}
    for article in arti:
        article_id = article.get('href')[-10:-4]
        print(article_id)
        if article_id in cards:
            continue
        else:
            article_title = article.find('h2', 'article-card-title').text.strip()
            article_link = URL[:-6] + article.get('href')
            cards[article_id] = {
                'title': article_title,
                'link': article_link
            }
            fresh_news[article_id] = {
                'title': article_title,
                'link': article_link
            }
    return cards, fresh_news



def jsoning(dict):
    with open('news_archive.json', 'w') as file:
        json.dump(dict, file, indent=4, ensure_ascii=False)



def main():
    get_content(URL)



if __name__ == '__main__':
    main()