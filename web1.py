#web2.py

from bs4 import BeautifulSoup

# 페이지 로딩
page = open('Chap09_test.html','rt',encoding='utf-8').read()

#검색 용이 스프객체
soup = BeautifulSoup(page, 'html.parser')

#전체보기
# print(soup.prettify())

#<p> 전체 검색
# print(soup.find_all('p'))
#<p> 첫번째 하나 검색
# print(soup.find('p'))

#조건검색 <p class="outer-text"
# 파이썬 키워드 충돌 회피 class
# print(soup.find_all('p', class_='outer-text'))

# print(soup.find_all('p', attrs={'class':'outer-text'}))

for tag in soup.find_all('p'):
    #text 속성을 지정
    title = tag.text.strip()
    title = title.replace('\n', '')
    print(title)