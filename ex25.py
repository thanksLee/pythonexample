d = {}

d.setdefault("sel", []).append("02")
d.setdefault("sel", []).append("서울")

print(d)

from collections import defaultdict

print()
d = defaultdict(list)

d["sel"].append("02")
d["sel"].append("서울")

print(d)

print()

d = defaultdict(set)
d["incheon"].add("032")
d["inchone"].add("인천")

print(d)

print()

color = [("파랑", 3), ("노랑", 2), ("빨강", 1), ("파랑", 4), ("노랑", 5)]

d = defaultdict(list)

for key, val in color:
    d[key].append(val)

li = list(d.items())

print(li)

print()

d = {}
for key, val in color:
    d.setdefault(key, []).append(val)

li = list(d.items())
print(li)

print("======================")

str = "hello hi goodmorning"

d = defaultdict(int)

for key in str:
    d[key] += 1

li = list(d.items())

print(li)

print("=========================================")

# dictionary에서 최소값/최대값/정렬

fruits = {
    "사과":300,
    "오렌지":200,
    "바나나":500,
    "배":1000,
    "포도":2000
}

# zip 함수를 이요해서 키(key) 와 값(value)를 뒤집니다.

max_fruits = max(zip(fruits.values(), fruits.keys()))

print("max : ", max_fruits)

min_fruits = min(zip(fruits.values(), fruits.keys()))

print("min : ", min_fruits)

sorted_fruits = sorted(zip(fruits.values(), fruits.keys()))
print("sorted : ", sorted_fruits)

# sorted_fruits = sorted(zip(fruits.values(), fruits.keys()), reversed)
# print("sorted : ", sorted_fruits)

print(min(fruits)) # 키를 비교하여 최소키를 리턴한다.
print(max(fruits))

print(min(fruits.values())) # 키를 비교하여 최소키를 리턴한다.
print(max(fruits))

print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")

print(min(fruits.values()))
print(max(fruits.values()))

# zip을 사용하지 않고 키와 값을 동시에 얻는다.

print("-----------------------------")
print(min(fruits, key = lambda n : fruits[n])) # min의 key 함수를 적용한 예
print(max(fruits, key = lambda n : fruits[n]))
print()
# 최소값과 일치하는 key를 얻어오고자 할때
max_val = max(fruits, key = lambda n: fruits[n])
print(max_val)

print()

fruits1 = {"사과":300, "오렌지":300}

#value가 동일값인 경우 key를 가지고 비교한다.
print(min(zip(fruits1.values(), fruits1.keys())))