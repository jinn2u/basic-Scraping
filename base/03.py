# ip확인 api로 접근해서 결과 출력하기
import urllib.request
url = 'http://api.aoikujira.com/ip/ini'
#데이터 읽어 들이기
res = urllib.request.urlopen(url)
data = res.read()
# 바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)
