# 로그인을 위한 모듈 추출하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정하기
USER = "test"
PASS = "test"
# 세션 시작하기 
session = requests.session()
# 로그인하기 
login_info = {
    "m_id": USER,  # 아이디 지정
    "m_passwd": PASS  # 비밀번호 지정
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # 오류가 발생하면 예외가 발생합니다.

# 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html" 
res = session.get(url_mypage)
res.raise_for_status()
# print(res.text)

# 마일리지와 이코인 가져오기 --- (※5)
# soup = BeautifulSoup(res.text, "html.parser")
# # print(soup)
# mileage = soup.select_one(".mileage_section1 span")
# ecoin = soup.select_one(".mileage_section2 span")
# # print("마일리지: " + mileage)
# print("이코인: " + ecoin)

# mileage = soup.select_one("#wrap_gnb > h1 > a").get_text()
# print(mileage)


# mileage = soup.select_one("#container > div > div.sm_myorder > table > tbody > tr > td.left > a")
# ecoin = soup.select_one(".mileage_section2 span")
# print(mileage)
# print(ecoin)