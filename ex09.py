# -*- coding:utf-8 -*-

ss = set(['a', 'b', 'c'])

print(ss)

ss = set([1, 2, 3, 5])

print(ss)

ss = set("Good Morning")

print(ss)

ss1 = set([1, 2, 3, 4])
ll = list(ss1)

print(ll, ll[2])

s1 = set([1, 2, 3, 4, 5, 6, 7, 8])
s2 = set([3, 5, 6, 7, 8, 9])

#교집합은 '&' 기호를 이용한다.
print(s1 & s2)

#합집합은 '|' 기호를 이용한다. 또는 union 함수를 이용한다.
print(s1 |s2)
print(s1.union(s2))

#차집합은 '-' 기호를 이용한다. 또는 differnce 함수를 이용한다.
print(s1-s2)

print(s1.difference(s2))

#집합에 값을 추가하기
s1 = set([1, 2, 3, 4, 5])
s1.add(100) # 한개의 값을 추가할때는 add를 이용한다.

print(s1)


s1 = set([1, 2, 3, 5])
s1.update([10, 100, 1000])
print(s1)


# 집합에서 값을 삭제하기
s1 = set([1, 2, 4, 3, 5]) 
print(s1)

s1.remove(4) 

print(s1)

# 대칭 차집합 : 두개의 집합이 있을때
s = set("Good Morning")
t = set("Good Night")

print(s^t)

s.remove('g')
try:
    s.remove('h')
except:
    print("error")    

s.discard('h')
s.discard('G')

length = len(s)
print(length)

print(s)



# 집합에서 모든 항목을 제거
s.clear()

print(s)

