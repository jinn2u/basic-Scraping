# 라이브러리 읽어들이기
import urllib.request
# url과 저장경로 지저하기
url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test2.png'
# 다운로드
urllib.request.urlretrieve(url,savename)
print('저장되었습니다----')