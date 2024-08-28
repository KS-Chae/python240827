#web1.py

from bs4 import BeautifulSoup

# 페이지 로딩
page = open('Chap09_Selector.html','rt',encoding='utf-8').read()

#검색 용이 스프객체
soup = BeautifulSoup(page, 'html.parser')
