# -*-coding:utf8-*-
print("-- 사용자 정의 함수 --")
print("")

def show_max(a, b):
    if a > b:
        print(a, "는 최대값이다.")
    elif a == b:
        print(a, "와", b, "는 같다")
    else:
        print(b, "는 최대값 이다.")


print(show_max(10, 6))

i = 5
j = 5

print(show_max(i, j))

i = 10
j = 100

print(show_max(i, j))

def sum(a, b):
    return a+b

print(sum(10, 20))

print("")
print("-- 예상할수 없는 인수를 갖는 함수 --")

def sum(*a):
    tot = 0
    for i in a:
        tot += i
    return tot

print(sum(10, 20, 30, 40))

def cal(aa, *a):
    tot = -1
    if aa == "sum":
        tot = 0
        for i in a:
            tot += i
    elif aa == "mul":
        tot = 1
        for i in a:
            tot *= i
    return tot

print(cal("mul", 1, 2, 1, 12))


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print (key, value)

kwargs = {"arg3": 3, "arg2": "two","arg1":5, "arg2":15, "arg3": 3, "arg2": "two","arg1":5, "arg2":15}
greet_me(**kwargs)

print("")
print("-- 리턴값의 유형 --")

def return_value(a, b):
    return a+b, a-b

print("")
print("-- return 만 단독으로 사용 --")

def showMsg(aa):
    if aa == 0:
        return
    print("0이 아니다")

print(showMsg(1))

print("")
print("-- 인수에 초기값을 설정하기 --")
print("  인수 초기화는 인수 선언의 제일 마지막에 처리")

def show(name, age, gender='M'):
    print("이름은 : ", name)
    print("나이는 : ", age)

    if gender == "M":
        print("남자")
    else:
        print("여자")

print(show("홍길동", 22))
print(show("홍길동", 21, 'F'))




def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print (key, value)

#kwargs = {"arg3": 3, "arg2": "two","arg1":5, "arg2":15, "arg3": 3, "arg2": "two","arg1":5, "arg2":15}
kwargs = {"arg3": 3, "arg2": 30, "arg4": 40, "arg5": 50, "arg6": 60}
greet_me(**kwargs)


