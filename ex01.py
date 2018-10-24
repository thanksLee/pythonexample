# -*- coding: utf-8 -*-
aa = 124
print(aa)

#bb = "안녕"
#print(bb)

cc = 23.22  #부동소수점
cc = 34.4E-3 # E표기법 : E뒤의 값이 10진수임을 표현 --> 34*10^-3을 의미
print(cc)

dd = 0xabc

a = 1
b = 10
c = 100

print("a + b : " +  str(a + b))
print ("a**b : " + str(a**b))
print("5%2 : " + str(5%2))
print("2%5 : " + str(2%5))

print("3/2 : " + str(3/2))
print("3//2 : " + str(3//2))

print(dd)

print("I'm OK!!")

''' 안녕하세요!!!
반갑습니다....
'''

print (u'''안녕하세요
반가워요
또만납시다''')


print(u"------ 문자열 합치기 ------")

a = "You've got "
b = "a friend"

print (a+b)

print(u"------ 문자열 곱하기 ------")
c = "hello"
c = c*3

print(c)

print("+"*30)
print("hello Python")
print("+"*30)

print(u"------ 문자열의 인덱싱과 슬라이싱 ------")
str = "You've got a friend "
print(str[0])
print(str[4])
print(str[3])
print(str[8])

str1 = str[-6] + str[-5] + str[-4]+ str[-3]+ str[-2]+ str[-1]

print("str1 : " + str1)

print(str[-4:-1])
print(str[-1:-6]) # 인덱스 -1에서 -6까지 슬라이스 하겠다.
print(str[-6:-1]) # 인덱스 -1에서 -6까지 슬라이스 하겠다.

print(str[-7:-1])

print(str[-6:])
print(str[:])   # str 문자열을 처음부터 끝까지 슬라이스 하겠다.


str2 = "20170601132334"

print("year : " + str2[:4])
print("month : " + str2[4:6])
print("day : " + str2[6:8])
print("date : " + str2[:8])
print("time : " + str2[8:])

# 문자열의 교체 방법

aa = "ABCD"
print(aa[1])

#aa[1] = "F" # 문자열, 튜플 자료형은 그 요소값을 변경할 수 없다.
#print(aa[1]) # TypeError: 'str' object does not support item assignment 오류 발생


print(aa[:1])
print(aa[2:])

print(aa[:1] + "F" + aa[2:])

############# 문자열 대입

# 숫자 대입
print(u"제 나이는 %d 살 입니다." %20)

print (u"제 나이는 %d 살 입니다." %21)

# 문자열 대입
print(u"제 이름은 %s 입니다." %"홍길동")

# 숫자형 변수로 대입하기
age = 50
print(u"제 나이는 %d 살 입니다." %age)

# 여러개의 값을 대입하기
name = "김말똥"
print(u"저의 이름은 %s 입니다. 나이는 %d 입니다." %(name, age))

print(u"완치될 확률은 %d%% 입니다. " %80)

# 포멧 코드의 활용예

# 소수점 표현하기
print("%0.5f" %120.45454534343434)
print("%1.5f" %120.45454534343434)
print("%-1.6f" %120.45454534343434)

# 정렬과 공백 처리

print("%10s" %"hello")
print("%-10s" %"hello")


print("%15sPython!!!" %"hello")   # 오른쪽 정렬 , 즉 공백을 왼쪽에 채우기
print("%-15sPython!!!" %"hello")  # 왼쪽 정렬, 즉 공백을 오른쪽에 채우기

# 리스트 (list)
#: 다른 언어의 배열과 같은 형을 의미한다.

# 리스트 예
aa = [10, 20, 30]
movies = ["트렌스포머", "국제시장", "명량"]
bb = [10, 20, "명량", "국제시장"]
cc = [10, 20, ["명량", "국제시장"]]
dd = []

print(cc)

# 리스트 내에는 어떠한 자료형도 포함시킬수 있다.

# [리스트의 인덱싱과 슬라이싱]
aa = [10, 20, 30]

print(aa[0])
print(aa[-1])  # 요소의 인덱스 값이 음수인 경우 뒤에서 부터 가리킨다.

print(aa)

print(aa[0] + aa[2])

bb = [10, 20, 30, ["ab", "bb", "ccd"]]

print(bb[0])
print(bb[-1])
print(bb[-1][1])


cc = [10, 20, ["aaa", "bbb", "ccc", ["국제시장", "평창"]]]

print(cc[2][3][0]) # 3중 리스트 구조

ab = [1, 10, 100, 1000, 10000]
print(ab[:3])
print(ab[-1:])

ab = "110100100010000"
print(ab[:3])

bc = [1, 10, 100, ["aa", "bb", "cc"], 1000, 10000]
print(bc[2:5])

print(bc[3][1:])

# 리스트 연산(+, * : 반복)
aa = [10, 20, 30]

bb = [100, 200, 300]

print(aa + bb)
print(aa*3)


# 리스트값 변경하기
print(aa[1])

aa[1] = 100  # 문자열, 튜플의 형의 요소값은 변경할 수 없지만, 리스트의 요소값은 변경할 수 있다.

print(aa)

print(aa[2:])

aa[2:] = ["국제시장", "명량"]
print(aa)

print(aa[1:3])
aa[1:3] = ["백", "천", "만", "십만"]

print(aa)

aa[4] = ["십만", "백만", "천만"] # 단일 요소로 대입할때는 리스트로 변경이 된다.

print(aa)


aa[1:4] = [] #요소삭제 : 인덱스 1 에서 4까지 삭제

print(aa)

del aa[0] # del 파이썬 내장함수를 이용한 삭제 방법 del 객체(모든 자료형)

print(aa)

print("")
print("")
print("----------튜플-------------")
print("")

##### 튜플..


# 튜플의 인덱싱, 슬라이싱, 연산
tu = ("a", "b", "c", 10, 100, 200)

print(tu[0])
print(tu[2:])

tu2 = ("d", "e", "f")
print(tu + tu2)
print(tu*3)

#del tu2[2] 튜플은 문자열과 마찬가지로 요소를 변경하는 것을 허용하지 않는다.

print("")
print("----------- 튜플 불린")
print("")

if[] :
    print("참")
else:
    print("거짓")


