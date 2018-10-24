# -*- coding:utf-8 -*-

number = 1
print(number);

print("")
print("-- 제어문 --")
print("")

if number:
    print("0이 아니다")
else:
    print("0", d)


x = 100
y = 1000

print(x > y)
print(x == y)


print("")
print("---- in 연산자 ----")
print("")


print("a" in ["a", "b", "c"])
print("a" not in ["a", "b", "c"])

"a" in ("a", "b", "c")
print("a" in "abcd")

aa = ["a", "b"]
flag = 0

if "a" in aa:
    print("a를 갖고 있습니다.")
else:
    if flag:
        print("a를 갖고 있습니다.")
    else:
        print("a를 갖고 있지 않습니다.")

# 좀더 간편하게 변경

if "c" in aa:
    print("c를 가지고 잇습니다.")
elif "a" in aa:
    print("a는 가지고 있고 c는 가지고 있지 않습니다.")
else:
    print("a와 c가 aa에 없습니다.")

print("")
print("---- pass 연산자 ----")
print("")

dd = "d"

if dd in aa:
    pass
else:
    print(dd + "는 없습니다.")


pp = ["a", "b", "c"]
if dd in pp : pass
else : print("없습니다.")

    