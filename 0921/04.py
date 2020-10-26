import urllib.request
import urllib.parse
API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

values = {
    'stnid':'184'
}
params = urllib.parse.urlencode(values)
# print(params) # stnid=184
# 요청 전용 url을 생성한다
url = API + '?' + params
# print('url=',url) # url= http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=184
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)

# 별도로 저장하기위해서
# 저장방법 1.
# savename = 'asd.txt'
# with open(savename,mode='wb') as f:
#     f.write(data) #바이너리만 읽을 수 있다.
#     print("저장되었습니다.")

#  저장방법 2.
# savename='asd.txt'
# urllib.request.urlretrieve(url,savename)