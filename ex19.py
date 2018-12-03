import collections

print(collections.Counter(["aa", "cc", "dd", "aa", "bb", "ee"]))

print(collections.Counter({"가" : 3, "나" : 2, "다" : 4}))

print(collections.Counter(a=2, b=4, c=1))

container = collections.Counter()

print(container)

container.update("aabcdeffgg")

print(container)

container.update({"c":2, "f":3})

print(container)

# Counter 접근하기

for n in "abdfeh":
    print('%s: %d' %(n, container[n]))


ct = collections.Counter("Hello jenny")
ct["x"] = 0

print(ct)

print(list(ct.elements()))

# most_common() 사용하기 : 상위 n개를 시퀀스로 만든다.

ct2 = collections.Counter()

with open("most_test.txt", "rt") as f:
    for li in f:
        print(li.rstrip().lower())
        ct2.update(li.rstrip().lower())

for item, cnt in ct2.most_common(10):
    print('%s, %2d' %(item, cnt))

print(ct2.most_common())


ct3 = collections.Counter(["a", "b", "c", "b", "a"])
ct4 = collections.Counter("aerocplane")

print("bbb : ", ct3)
print("aaa : ", ct4)

print(ct3 + ct4)
print(ct3 - ct4)
print(ct3 & ct4) # 교집합
print(ct3 | ct4) # union all

# defaultdict 메서드는 컨테이너를 초기화 만들때 default 값을 지정한다.

def default_aa():
    return "aa"

dic = collections.defaultdict(default_aa, n1 = "하3이")

print(dic)
print(dic['n1'])
print(dic['n2'])
print(dic['n3'])

# Deque = 양방향 큐(데크)는 컨테이너 양쪽 (앞뒤)에 아이템을 넣거나 뺄수 있다.

deq = collections.deque("Hello python")

print(deq)
print(len(deq))
print(deq[0]) # 오른쪽 부터
print(deq[-1]) # 왼쪽부터

deq.remove("o")
print(deq)

deq.append("k")
print(deq)

deq.appendleft("jj")
print(deq)

deq1 = collections.deque()
deq1.extend("가나다라마바사")

print(deq1)

deq1.append("아")
print(deq1)

deq1.extendleft("자")
print(deq1)

# 아이템 꺼내기
# 오른쪽에서 부터 꺼내오기
"""
while True:
    try:
        print(deq1.pop(), end=' ')
    except IndexError:
        break
"""

# 왼쪽에서 부터 꺼내오기
while True:
    try:
        print(deq1.popleft(), end=' ')
    except IndexError:
        break

# namedtuple()

print('')

aa = ("홍길동", 24, "남")

print(aa)

bb = ("강복녀", 21, "여")

print(bb[0])

for n in [aa, bb]:
    print('%s은(는) %d 세의 %s성 입니다.' %n)

Person = collections.namedtuple("Person", "name age gender")

aa = Person(name="홍길동1", age=25, gender="남" )
bb = Person(name="홍길동2", age=24, gender="여" )

print(aa, bb)

for n in [aa, bb]:
    print("%s는(은) %s세의 %s성입니다." %n)

# OrderedDict : 자료의 순서를 기억하는 사전형 클래스
dic = {}

dic["경기"] = "의정부"
dic["서울"] = "강남"
dic["부산"] = "광안리"
dic["대구"] = "몰라"
dic["제주"] = "남양주"

for i, j in dic.items():
    print(i, j)

print("--------------------------------------")
dic1 = collections.OrderedDict()
dic1["경기"] = "의정부"
dic1["서울"] = "강남"
dic1["부산"] = "광안리"
dic1["대구"] = "몰라"
dic1["제주"] = "남양주"

for i, j in dic1.items():
    print(i, j)


import array
from pprint import pprint

str = "abcdefghijklmn"

arr = array.array("u", str) # array(타입코드, 값) : https://docs.python.org/3/library/array.html

print(arr)

print(array.typecodes)

arr1 = array.array("i", range(5))

print(arr1)

arr1.extend(range(5))

print(arr1)

print(arr1[3:6])

print(list(enumerate(arr1)))
print("================================")
# array 의 내용을 파일에 쓰거나 읽기
import binascii

arr = array.array("i", range(5))

print(arr)

# tofile(파일객체) : 파일개체에 쓰는 함수

f = open("test.txt", "w+b")

arr.tofile(f)
f.flush()

with open("test.txt", "rb") as f1:
    data = f1.read()
    
    # 아래 내용은 생략 가능. 주석처리함.
    #print(binascii.hexlify(data))

    # 파일을 오픈하여 제일 마지막까지 읽었으므로 다시 읽으려면 포인터를 제일 처음으로
    # 읽으려면 seek() 함수를 이용하자
    f1.seek(0)
    arr2 = array.array("i")
    arr2.fromfile(f1, len(arr))

    print(arr2)