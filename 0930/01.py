from urllib.parse import urljoin
base = "http://example.com/html/a.html"
print(urljoin(base, "b.html"))
print(urljoin(base, "sub/c.html"))
print(urljoin(base, "../index.html"))
# http, https, //로 시작하면 그것으로 대체한다.
print(urljoin(base, "http://otherExmaple.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))