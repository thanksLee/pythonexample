def generatorEx(n):
    for i in range(n):
        yield i ** 2


gen = generatorEx(4)
print(gen)

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

gen = generatorEx(3)
print(next(gen))
print("========================")

def countdown(n):
    while n > 0:
        yield n
        n -= 1
    print("end")


cnt = countdown(3)
print(cnt)
print(next(cnt))
print(next(cnt))
print(next(cnt))

print("========================")

for i in generatorEx(5):
    print(i)


from collections import deque

dQ = deque(maxlen = 4)

dQ.append("aa")
dQ.append("bb")
dQ.append("cc")
dQ.append("dd")


print (dQ)

dQ.append("ee")

print(dQ) # 새로운 아이템 ee가 추가되면서 aa 아이템은 자동으로 삭제

dQ.append("gg")
dQ.append("hh")
dQ.append("11")

print(dQ)


def search_word(lines, find_word, history = 4):
    previous_line = deque(maxlen=history)
    for readline in lines:
        if find_word in readline:
            yield readline, previous_line
        previous_line.append(readline)

with open("someText.txt", encoding="UTF8") as f:
    fword = search_word(f, "꽃", 4)
    print(fword)
    print(next(fword))

    print(next(fword))
    print(next(fword))
    print(next(fword))
    print(next(fword))
    print(next(fword))


print("")

if __name__ == "__main__":
    with open("someText.txt", encoding="UTF8") as f:
        for fline, prevTexts in search_word(f, "꽃", 4):
            for preline in prevTexts:
                print("preline : ", preline)
            print("fline : ", fline)
            print("="*10)
