import requests
from bs4 import BeautifulSoup


URL = "https://kaktus.media/?lable=8&date=2022-05-07&order=time"

HEADERS = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

html = get_html(URL)
# print(html.text)

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="ArticleItem")
    news = []
    for item in items:
        news.append({
            'title' : item.find('a', class_="ArticleItem--name").getText().replace('\n', ''),
            'time' : item.find('div', class_='ArticleItem--time').getText().replace('\n', ''),
            'link' :item.find('a', class_="ArticleItem--name").get('href')
        })
    return news

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        ans = get_data(html.text)
        return ans
    raise Exception("Error in parser")