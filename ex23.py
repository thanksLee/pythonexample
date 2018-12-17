# unpacking

pa = (1, 2)
a, b = pa
print(a, b)


li_data = ["홍길동", 23, "서울", (1980, 11, 21)]
name, age, local, birth = li_data

print(name)
print(age)
print(local)
print(birth)

name, age, local, (year, month, day) = li_data

print(year)
print(month)
print(day)

str = "Hello"

a, b, c, d, e = str

print(b)

print()

# _ 사용시 필요한 데이터만 가져온다.
name, _, local, _ = li_data

print(local)

# 특정값을 무시하거나 *를 이용하여 여러개를 언패키하기
person_info = ("장기산", "aaa@naver.com", "010-0000-0000", "02-000-1111")

name, email, *phone = person_info

print(name)
print(email)
print(phone)

pointValue = [10, 5, 12, 11, 22, 14, 12, 15, 10, 10, 15, 14, 45]

*lastPoint, curPoint = pointValue

print(curPoint)
print(lastPoint)
print()
print()

address = [("우", 234, 123), ("도", "서울"), ("도", "경기"), ("우", 123, 134)]


def show_zipcode(num1, num2):
    print("우", num1, num2)

def show_local(str):
    print("도", str)

for key, *arg in address:
    if key == "우":
        show_zipcode(*arg)
    elif key == "도":
        show_local(*arg)


str2 = "홍길동/23/12123123132/123123123123123123123123/서울"

name, age, *num, local = str2.split("/")
print()
print(name)
print(age)
print()


li_data = ["홍길동", 23, "서울", (1980, 11, 21)]

name, *_, (year, *_) = li_data

print(name)
print(year)
