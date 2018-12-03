import tempfile
from tempfile import TemporaryFile

fp = tempfile.mktemp() # 임시파일 생성

print(fp)

f = tempfile.TemporaryFile() # w+b의 모드 (메모리에 임시 공간 생성)
print(f)

f = TemporaryFile("w+t")
f.write("하이 파이썬")
#print(f)
f.close()



with TemporaryFile("w+t") as f:
    f.write("하이 파이썬 \n")
    f.seek(0)
    data = f.read()

print(data)


import time

print(time.time())

print(time.localtime())

t = time.time()

print(time.localtime(t))

print(time.gmtime())
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
print(time.asctime())

print("jjjjjjjjjjjjjjjjjj")
print(time.strftime('%x'), time.localtime(time.time()))
print(time.strftime('%c'), time.localtime(time.time()))

for i in range(10):
    print(i)
    #time.sleep(1)

import calendar

print(calendar.calendar(2018))

print("aaa : ", calendar.prmonth(2018, 12))

print(calendar.weekday(2018, 7, 21))

print(calendar.monthrange(2018, 12))

import random

print(random.random())

print(random.randint(1, 10))

print(random.randint(10, 50))

def pop_list(data):
    n = random.randint(0, len(data)-1)
    return data.pop(n)

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    while data : print(pop_list(data))


from pprint import pprint
data = [(1, {"a":"가", "b":"나", "c":"다", "d":"라"}), 
        (2, {"e":"마", "f":"바", "g":"사", "h":"아"}), 
        ]


print(data)
pprint(data)
