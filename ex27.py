# 데이터베이스 자료를 딕셔너리에 저장 후 정렬 시키는 방법

records = [
    {"id":"test", "pw":"1234", "name":"홍길동", "hp":"010-1234-1234"},
    {"id":"test1", "pw":"12341", "name":"홍길동1", "hp":"010-1234-1234"},
    {"id":"test2", "pw":"12342", "name":"홍길동", "hp":"010-1284-1234"},
    {"id":"test3", "pw":"12343", "name":"홍길동3", "hp":"010-1234-1234"},
    {"id":"test4", "pw":"12344", "name":"홍길동4", "hp":"010-1234-1234"}
]

# 모듈 operatoer.itemgetter

from operator import itemgetter
from pprint import pprint
from collections import Counter

rec_by_name = sorted(records, key=itemgetter('name'))
rec_by_id   = sorted(records, key=itemgetter('id'))

pprint(rec_by_name)

rec_by_name_tel = sorted(records, key=itemgetter('name', 'hp'), reverse=True)
pprint(rec_by_name_tel)

# 데이터베이스 group by 절과 같은 기능 수행
# itertools.groupby() 를 이용하여 필드에 따라 레코드를 묶어주기

records = [
    {"addr":"서울 강남구", "order":"01-1000"},
    {"addr":"서울 강남구1", "order":"03-1000"},
    {"addr":"서울 강남구2", "order":"01-1000"},
    {"addr":"서울 강남구3", "order":"03-1000"},
    {"addr":"서울 강남구", "order":"01-1000"},
    {"addr":"서울 강남구", "order":"01-1000"},
    {"addr":"서울 강남구3", "order":"02-1000"},
    {"addr":"서울 강남구5", "order":"03-1000"},
    {"addr":"서울 강남구6", "order":"07-1000"},
    {"addr":"서울 강남구", "order":"01-1000"}
]

print()
print()
print()
print()
print("===========================================")
print()
print()

from operator import itemgetter
from itertools import groupby

records.sort(key = itemgetter("addr"))
pprint(records)
print()
print()
records.sort(key = itemgetter("order"))
pprint(records)

print()
print()

for addr, items in groupby(records, key=itemgetter('addr')):
    print(addr, len(list(items)))
    for item in items:
        print("___", item)


