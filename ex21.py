import random, bisect

random.seed(1) # 지속적인 난수 발생시 같은 난수를 발생시키고자 할때 사용

for i in range(5):
    print("%5.4f" %random.random(), end=" ")

print(" ")
print("New    Index   List : ")
print("====== ======= ====== : ")

li = []
for i in range(1, 15):
    rnd = random.randint(1, 100)
    pos = bisect.bisect(li, rnd) # 아이템이 추가 되었을때 인덱스 값 리턴
    bisect.insort(li, rnd) # 리스트를 정렬 상태로 유지시키는 함수
    print("%3d     %3d    " %(rnd, pos), li)
    #print(rnd, end = " ")

print("====== ======= ====== : ")

print(" ")
print("New    Index   List : ")
print("====== ======= ====== : ")

li = []
for i in range(1, 15):
    rnd = random.randint(1, 100)
    pos = bisect.bisect_left(li, rnd) # 아이템이 추가 되었을때 인덱스 값 리턴
    bisect.insort_left(li, rnd) # 리스트를 정렬 상태로 유지시키는 함수
    print("%3d     %3d    " %(rnd, pos), li)
    #print(rnd, end = " ")

print("====== ======= ====== : ")

