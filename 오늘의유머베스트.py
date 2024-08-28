# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        try:
                #클리앙의 중고장터 주소 
                data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
                #웹브라우져 헤더 추가 
                req = urllib.request.Request(data, headers = hdr)
                data = urllib.request.urlopen(req).read()
                
                #한글이 깨지면 디코딩
                page = data.decode('utf-8', 'ignore')
                soup = BeautifulSoup(page, 'html.parser')
                list = soup.findAll('td', attrs={'class':'subject'})

# <a href="/board/view.php?table=bestofbest&amp;no=476675&amp;s_no=476675&amp;page=2" target="_top">'반값 청년주택' 반대하는 주민들</a>

                for item in list:
                        try:
                                title = item.find('a').text

                                # print(title)
                                if (re.search('한국', title)):
                                        print(title.strip())
                        except:
                                pass
        except:
                pass
