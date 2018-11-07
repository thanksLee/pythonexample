# -*- coding:utf8 -*-


fp = open("test_new.txt", 'w')
fp.close()

fp = open("test_new.txt", 'w', encoding="utf-8")

for i in range(5):
    content = "%d 번째 줄 .. \n" %i
    fp.write(content)

fp.close()

# 파일 읽어오기

fp = open("test_new.txt", 'r', encoding="utf-8")
while True:
    data = fp.readline() # 더이상 읽어올 라인이 없다면 None을 리턴
    if not data:
        break
    print(data)

fp.close()


while 1:
    userData = input()
    if not userData: break
    print(userData)

fp = open("test_new.txt", "r", encoding="utf-8")
datas = fp.readlines()

for data in datas:
    print(data)

fp.close()


fp = open("test_new.txt", "r", encoding="utf-8")
data = fp.read()

print(data)

fp.close()



fp = open("test_new.txt", "a", encoding="utf-8")

for i in range(5, 8):
    data = '%d 번째 라인 \n' %i
    fp.write(data)

fp.close()

with open("test_2.txt", "w", encoding="utf-8") as fp:
    fp.write("with문을 이용한 파일 입출력 테스트")

import sys

args = sys.argv[1:] # 첫번째 인자 - 실행시 ex07.py test 연습 몰라
                    # 여기서 test : 0번째 인자, 연습 : 1번째 인자, 몰라 : 2번째 인자

for i in args:
    print(i)
    