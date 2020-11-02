# JSON 사용하기

import json

price = {
    'data': '2019-10-18',
    'price':{
        'apple': 80,
        'orange': 50,
        'banana': 40
    }
}
#dumps를 사용하면 dictionary를 json형태로 변환한다.
s = json.dumps(price)
print(s)
print(type(s))