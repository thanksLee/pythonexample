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
    time.sleep(1)

