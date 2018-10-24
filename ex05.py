# -*- coding: utf-8 -*-

print("")
print("-- 문자열 --")
print("")

print("You've {1} a friend".format("got", "yes"))

# {n}는 자리표시자를 의미한다. 여기서 n은 숫자를 말한다.
# format()에 지정된 위치를 표시한다.
str = "{2} {0} {1}".format("a", 100, 200)

print(str)

number = 100
day = "sunday"

print("오늘은 우리가 사귄지 {0}일 째 되는 날!! 요일은 {1}!!!".format(number, day))


print("")
print("-- 인덱스와 이름 혼용 --")
print("")

print("오늘은 우리가 사귄지 {0}일 째 되는 날!! 요일은 {day}!!!".format(300, day="saturday"))

print("")
print("-- 좌측 정렬 --")
print("")

name = "이병훈"
print("{0:<10}".format(name))

print("")
print("-- 우측 정렬 --")
print("")

name = "이병훈"
print("{0:>10}".format(name))

print("")
print("-- 가운데 정렬 --")
print("")

name = "이병훈"
print("{0:^10}".format(name))
print("{0:^20}".format(name))

print("")
print("-- 소문자를 대문자로 바꾸는 함수 --")
print("")

aa = "hello"

aa1 = aa.upper()

print(aa1)

print("")
print("-- 대문자를 소문자로 바꾸는 함수 --")
print("")

aa2 = "HELLO"

print(aa2.lower())

print("")
print("-- 문자 갯수를 리턴하는 함수 --")
print("")

aa = "abdcde"
cnt = aa.count("d")
print(cnt)

print("")
print("-- 문자열의 기이 구하는 함수 --")
print("")

cnt = len(aa)
print(cnt)

print("")
print("-- 문자 위치 찾기 함수 : 문자열에서 찾고자하는 문자의 첫번째 위치를 리턴하는 함수 --")
print("")

bb = "adfadfadsfadf"
loc = bb.find("f") # 찾고자 하는 문자가 없는 경우에는 -1을 반환한다.

print(loc)

loc = bb.index("d") # index 함수는 find함수와는 다르게 찾고자 하는 문자가 없을 경우 에러가 난다.
print(loc)


print("")
print("-- 공백지우기 함수 --")
print("")

aa = "   goood   "
print("[" + aa.lstrip() + "]")

print("[" + aa.rstrip() + "]")

print("[" + aa.strip() + "]")


print("")
print("-- 문자열 대체 함수 --")
print("")


# 문자열 대체함수(replace) : 문자열 내의 특정한 값을 다른 값으로 교체한다.
aa = "good morning Jane!!"
aa1 = aa.replace("morning", "night") # 바뀔 대상(문자열), 교체할 문자열

print(aa1)


print("")
print("-- 문자열 나누기(Split) --")
print("")

str = "good morning   jane!!"
str_sp = str.split() # 괄호안에 값이 없으면 공백을 기준으로 문자열을 나눈다.

print(str_sp)


str = "이병훈/30/서울시 강남구/0101-1111"
str_sp = str.split("/") # '/'를 구분자로 해서 문자열을 나눈다. 그 결과는 리스트에 저장된다.


print(str_sp)


print("")
print("-- 리스트에 값 추가하기 --")
print("")

li = [10, 100, 1000, 10000]

li.append(11)

print(li)


li.append("ab")

print(li)

li.append(['a', 'b'])

print(li)

print("")
print("-- 리스트 정렬함수 --")
print("")

li = [1, 5, 10, 2, 7, 3]
li.sort()
print(li)

print("")
print("-- 리스트 뒤집기 함수 --")
print("")

li.reverse() # sort()함수를 적용후 reserve()를 사용하면 내림차순 정렬이 한다.

print(li)


print("")
print("-- 요소의 위치를 반환하는 함수 --")
print("")

li = ['b', 'a', 'f', 'c']

aa = li.index('a')
print( aa)
'''
aa = li.index(1)
print(aa)
'''

print("")
print("-- 요소를 삽입하는 함수 함수 --")
print("")

aa = [1, 2, 3, 4]
aa.insert(2, 5) # append 함수는 무조건 뒤에 추가시키지만, insert 함수는 원하는 위치에 추가 시킬수 있다.

print(aa)

print("")
print("-- 요소를 제거하는 함수 --")
print("")

cc = [23, 13, 3, 6, 19, 3]
cc.remove(3) # 지우고자하는 첫번째 값을 제거한다.
cc.remove(3)
print(cc)

print("")
print("-- 요소를 끄집어 내는 함수 --")
print("")


dd = [23, 12, 3, 6, 5, 3]
aa = dd.pop() # () 안에 값이 없을 경우 리스트상의 마지막 값을 가져온다.
print(aa)

aa = dd.pop(1) # pop() 리스트의 요소(값)을 끄집어내고, 끄집어낸 요소는 리스트에서 삭제한다.
print(aa)

print("")
print("-- 요소의 갯수를 파악하는 함수 --")
print("")

dd = [23, 12, 3, 6, 5, 3]
cnt = dd.count(3) # coutn(요소)의 갯수를 구하는 함수
print(cnt)

print("")
print("-- 리스트 확장함수 함수 --")
print("")

a = [1, 2, 3]
print(a)


a += [2, 3, 4, 5, 6]
print(a)