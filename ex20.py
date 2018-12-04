import heapq
from showHeap import show_tree
from heapData import data


heap1 = []

for n in data:
    print("%3d push : " %n)
    heapq.heappush(heap1, n)
    show_tree(heap1)


print("=======================")

heapq.heapify(data)
show_tree(data)


print("=======================")

# heap data 접근

for n in range(3):
    print("------- : ", n)
    minVal = heapq.heappop(data)
    show_tree(data)
    print(minVal)

print("=======================")
print("=======================")
print("=======================")

# heap replace
data = [10, 8, 5, 4, 6, 9]
heapq.heapify(data)
show_tree(data)


for n in [3, 15]:
    min_val = heapq.heapreplace(data, n)
    print(min_val)
    show_tree(data)


print("-----------------------------")
print("-----------------------------")
print("-----------------------------")

# 힙의 최대/최소 값 구하기 : nlargest(), nsmallest()
data = [10, 8, 5, 4, 6, 9]
print(heapq.nlargest(2, data))