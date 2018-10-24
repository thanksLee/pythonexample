# -*- coding: utf-8 -*-

aa = 0
while aa < 10:
    aa = aa + 1
    print("aa 값은 %d 입니다." %aa)
    if aa == 10:
        print("종료합니다.")

print("")
print("---- 무한루프의 예 ------")
print("")

#while 1:
#    print("무한루프")


print("")
print("---- 보조제어문 ------")
print("")

m = 100
n = 10
while m:
    n = n - 1
    print("현재 %d 입니다." %n)

    if not n:
        print("n의 값은 0 입니다.")
        break


# 1부터 10까지의 정수중 홀수를 출력하는 코드
i = 0
while i < 100:
    i = i + 1
    print(i%2)
    if i%2 == 0 : continue
    #print(i)

print("")
print("---- for 문 ------")
print("")

list1 = ["a", "b", "c"]

for i in list1:
    print(i)

jumsu = [90, 50, 60, 70, 80]

number = 0

for i in jumsu:
    number = number + 1
    if i >= 60: print("%d번 학생의 점수는 %d 합격되었습니다... !" %(number, i))
    else: print("%d번 학생d의 점수는 %d 불합격되었습니다." %(number, i))


# continue
number = 0
for i in jumsu:
    number = number + 1
    if i < 60: continue
    print("%d 번 학생 합격입니다." %number)

aa = [("a", "b"), ("c", "d"), ("e", "f")]
for(i, j) in aa:
    print(i + j)


for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print(" ")


print("")
print("-- range --")
print("")


for i in range(1, 5):
    print(i)
else:
    print("반복문 종료")


print("")
print("-- 구구단 --")
print("")


for i in range(2, 10):
    for j in range(1, 10):
        print("%d*%d=%d" %(i, j, i * j), end = " ")
    print(" ")

print("")
print("-- 리스트안에 for문을 이용하여 프로그램 해보기 --")
print("")

aa = [1, 2, 3, 4, 5, 6, 8, 9]
gugudan_2 = []

for i in aa:
    gugudan_2.append(i*2)
print(gugudan_2)

gugudan_2 = [i*2 for i in aa]

print(gugudan_2)


print("")
print("-- 5단의 결과값 중에서 짝수만 리스트에 추가하는 예 --")
print("")

gugudan_2 = [i*5 for i in aa if i % 2 == 0]

print(gugudan_2)

print("")
print("-- 구구단의 결과를 저장하는 리스트 구현 --")
print("")

gugudan = [i*j  for i in range(2, 10)
                for j in range(1, 10) ]
print(gugudan)                
