import queue

q = queue.Queue()

for i in range(3):
    q.put(i)
    print("jjjj : ", i)

while not q.empty():
    print(q.get(), end=" ")

print()

lq = queue.LifoQueue()
for i in range(5):
    lq.put(i)
    print("jjj : ", i)

while not lq.empty():
    print(lq.get(), end=" ")


print()

print("======================================")


import heapq

class PriorityQueue:
    def __init__(self):
        self.list = []
        self.idx = 0
    
    def put(self, item, priority):
        heapq.heappush(self.list, (-priority, self.idx, item))

        self.idx += 1
    
    def pop(self):
        heapq.heappop(self.list)


class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Item({!r})".format(self.name)
         # !r은 repr() 호출하는 것과 같다. !s 은 str()호출하는 것과 같다. !a은 ascii로 변환

pQ = PriorityQueue()

pQ.put(Item("홍길동"), 1)
pQ.put(Item("장길산"), 2)
pQ.put(Item("임꺽정"), 3)
pQ.put(Item("일지매"), 3)

print(pQ.list)

print(pQ.pop)