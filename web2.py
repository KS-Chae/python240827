#web2.py

# 웹서버와 통신
import requests

from bs4 import BeautifulSoup

url = 'https://www.daangn.com/fleamarket/'
response = requests.get(url)

#검색 용이 스프객체
soup = BeautifulSoup(response.text, 'html.parser')

f = open('daangn.txt', 'a+', encoding='utf-8')

posts = soup.find_all('div', attrs = {'class':'card-desc'})
for post in posts:
    titleElem = post.find('h2', attrs={'class':'card-title'})
    priceElem = post.find('div', attrs={'class':'card-price'})
    addrElem = post.find('div', attrs={'class':'card-region-name'})
    #문자열만 추출
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    #f-string 방식
    print(f'{title}, {price},{addr}')
    f.write(f'{title}, {price},{addr}\n')
