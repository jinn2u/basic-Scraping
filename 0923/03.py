from bs4 import BeautifulSoup

html = """
<html>
    <body>
    <ul>
       <li><a href="http://www.naver.com">네이버</a></li>
       <li><a href="http://www.daum.net">디음</a></li>
    </ul>
    </body>
</html>
"""

#html 분석하기 
soup = BeautifulSoup(html, 'html.parser')  

#find_all()메소드로 추출하기
links = soup.find_all('a')  #모든 a태그를 list형태로 저장한다.
# print(links)

#링크 목록 출력하기
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">",href)
#  결과
# 네이버 > http://www.naver.com
# 디음 > http://www.daum.net