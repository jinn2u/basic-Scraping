import sys
import urllib.request as req 
import urllib.parse as parse
# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print('USAGE: download-forecast-argv <Region Number>')
    sys.exit()
regionNumber = sys.argv[1]
# 매개변수를 URL 인코딩합니다.
API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
values = {
    'stnid': regionNumber
}
params = parse.urlencode(values)
# print(params) # stnid=184
# 요청 전용 url을 생성한다
url = API + '?' + params
# print('url=',url) # url= http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=184
data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)
