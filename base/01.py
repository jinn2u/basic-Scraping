# 라이브러리 읽어들이기
import urllib.request

# url불러들이기
url = 'http://uta.pw/shodou/img/28/214.png'

# 저장이름 지정하기
savename = 'test2.png'

# 다운로드
urllib.request.urlretrieve(url,savename)

print('저장되었습니다----')
