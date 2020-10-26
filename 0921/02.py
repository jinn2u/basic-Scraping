import urllib.request

url = 'http://uta.pw/shodou/img/28/214.png'

savename = 'test3.png'
#다운로드
men = urllib.request.urlopen(url).read()
# print(men) #=>binary형태로 나온다.

# binary 형태의 savename을 write한다
with open(savename,mode='wb') as f:
    f.write(men)
    print("저장되었습니다.")

# with open as f 를 하면 자동으로 파일을 닫아준다.
# f는 open(…)함수가 리턴한 file object가 되는것이다.
# f = open(...)의 f와 같다.
# f = open(...)을 한다면 무조건 닫아줘야 한다. f.close()