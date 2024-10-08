#DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹서버와 통신
import requests
# 크롤링
from bs4 import BeautifulSoup

#디자인 파일 로딩
form_class = uic.loadUiType('DemoForm2.ui')[0]

#윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    #초기화 루틴
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    
    #슬롯메서드
    def firstClick(self):
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
        f.close()
        self.label.setText('당근 마켓 크롤링 완료')

    def secondClick(self):
        self.label.setText('두번째 화면 출력')
    def thirdClick(self):
        self.label.setText('세번째 화면 출력')


#직접 모듈을 실행했는지 체크(진입점 체크)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()