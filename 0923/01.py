from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>스크레이핑이란?</h1>
        <p>웹 페이지를 분석하는 것</p>
        <p>원하는 부분을 추출하는 것</p>
    </body>
</html>
"""

#html 분석하기 
soup = BeautifulSoup(html, 'html.parser')  
# print(soup)  #html코드가 그대로 나온다

#원하는 부분 추출하기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
# print(h1)
# print(p1)
# print(p2)
#  결과
# <h1>스크레이핑이란?</h1>
# <p>웹 페이지를 분석하는 것</p>
# <p>원하는 부분을 추출하는 것</p>

#요소의 글자 출력하기
print("h1 = "+h1.string)
print("p1 = "+p1.string)
print("p2 = "+p2.string)
#  결과
# h1 = 스크레이핑이란?
# p1 = 웹 페이지를 분석하는 것
# p2 = 원하는 부분을 추출하는 것