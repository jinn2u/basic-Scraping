from bs4 import BeautifulSoup
import urllib.request as req
import sqlite3

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# 데이터베이스 연결하기
filepath = "test.sqlite"
conn = sqlite3.connect(filepath)

# 테이블 생성하기 
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items") 
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT)""")
conn.commit()

def findDataAndInsert(selector):
    # print(sel_list)를 하게 되면 태그들과 안의 내용들이 같이 보이게 된다. type은 list이다.
    sel_list = soup.select(selector)  
    for a in sel_list:
        #증보판은 시집의 이름이 아니므로 건너뛴다.
        if a.string == '증보판': continue
        cur = conn.cursor()
        cur.execute("INSERT INTO items (name) VALUES (?)", [a.string])
        conn.commit()

findDataAndInsert("#mw-content-text > div > ul > li a ")

cur = conn.cursor()
cur.execute("SELECT * FROM items WHERE item_id <=10")
lists = cur.fetchall()
for a in lists:
    print(a)