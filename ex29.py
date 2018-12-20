# comprehension : list comprehension, Dictionary comprehension, set comprehension

# list comprehension

aa_li = [24, 1, 5]

aa_com = [item*3 for item in aa_li]

print(aa_com)

# dictionary comprehension

aa_dict = {"홍길동":100, "강호동":200, "유재석":300}

aa_dict_com = {value:key for key, value in aa_dict.items()}

print(aa_dict_com)
print()
print()
#set comprehension
aa_set = set(range(10))

print(aa_set)
aa_set_com = {i**2 for i in aa_set}

print(aa_set_com)

aa_set_com1 = {i for i in aa_set if i%2 == 0}
print(aa_set_com1)

# 꼭 대상이 set 일 필요는 없다. 시퀀스라면
aa_set_com2 = {2**i for i in range(10)}
print(aa_set_com2)

a = dict(one = 1, two = 2, three = 3)
print(a)

# dictionary의특정 부분을 이용해서 새로운 딕셔너리를 만들기
stock = {
    "삼성":100,
    "현대":90,
    "기아":80,
    "대우":70,
    "아모레":120,
    "코리아나":60,
    "한국화장품":80
}

st1 = {key:value for key, value in stock.items() if value >= 100}

print(st1)

stock_car = {key for key, value in stock.items()}

print(stock_car)

stock_car_key = {"삼성", "현대", "기아", "대우"}

stock_car = {key:value for key, value in stock.items() if key in stock_car_key}

print(stock_car)

# 성능면에서 속도가 떨어지므로 위의 방법을 사용하는 것이 현명하다.
stock_car1 = {key:stock[key] for key in stock.keys() & stock_car_key}
print(stock_car1)


# dict() : 사전 객체를 만들어 줌

aa = dict(a = 1, b = 2, c = 3)

print(aa)

abc = dict([("aa", 11), ("bb", 22), ("cc", 33)])

print(abc)

print()
print()

st1 = {key:value for key, value in stock.items() if value >= 100}

print(st1)

# 위의 내용과 비교했을때 속도가느리다.
stock_car1 = dict((key, value) for key, value in stock.items() if value >= 100)

print(stock_car1)
print()
print()

# collections.namedtuple() : 튜플 객체에 이름을 설정하는 함수
# dict 보다 메모리를 덜 사용한다.

from collections import namedtuple

Member = namedtuple('Member', ['email', 'date'])

member1 = Member('aaa@naver.com', '2015-11-22')

print(member1)

print(member1.email)
print(member1.date)
print(len(member1))
print()
print()

# unpacking
email, date = member1
print(email, date)
print()
print()

stock = ("삼성", 10, 100)

def cal_stock(stock):
    tot = 0
    for n in stock:
        tot = stock[1] * stock[2]
    return tot

print(cal_stock(stock))
print()
print()

stock_rec = [
    ("삼성", 10, 100),
    ("현대", 10, 90),
    ("기아", 10, 80)
]

def cal_stock1(stock):
    tot = 0
    for n in stock:
        tot = n[1] * n[2]
    return tot

print(cal_stock1(stock_rec))


Stock = namedtuple('Stock', ['name', 'amount', 'price'])

def cal_stock2(stock):
    tot = 0
    for n in stock:
        s = Stock(*n)
        print(s) # 튜플을 분리
        tot += s.amount* s.price
    return tot

print(cal_stock2(stock_rec))
print()

n1 = ("삼성", 10, 100)
print(*n1) # 튜플을 분리

print()
print()
print("================================================")
print()

# namedtuple은 수정 할 수 없다.

stock2 = Stock('기아차', 100, 500)
print(stock2)

print(stock2.amount)

# 아래 내용은 에러 발생
#stock2.amount = 120

stock2 = stock2._replace(amount=120)

print(stock2.amount)

# _replace()를 활용해서 prototype tuple을 만들 수 있다.

Stock3 = namedtuple('Stock3', ['name', 'amount', 'price', 'date', 'time'])

# 프로토타입 인스턴스 생성
prototype_stock = Stock3('', 0, 0, None, None)

# dictionary를 tuple로 함수로 만들기
def dict_to_stock(dic):
    return prototype_stock._replace(**dic)

aa = {"name":"삼성", "amount":200, "price":100}

aa_stock = dict_to_stock(aa)

print(aa_stock)


def show_param(*s):
    print(s)
    for p in s:
        print(p)

show_param("a", 21, 1, "b")

def show_param2(**dic):
    print(dic)
    print(dic.keys())
    print(dic.values())

    for key, value in dic.items():
        print("%s, %s" %(key, value))


show_param2(one=1, two=2, three=3, four=4)
print()
print()
print()
def show_param3(*s, **ss):
    print(s)
    print(ss)

show_param3("a", "b")

print()
print()

show_param3(one=1, two=2)

print()
print()

show_param3("a", "b", one=1, two=2)

print()
print()
ss2 = {'c':1, 'd':2, 'e':3}

show_param2(**ss2)

# ChainMap 클래스 : 여러개의 딕셔너리(매핑데이터)가 있을때 하나의 딕셔너리로
#                    합쳐서 검색을 할때 사용한다.



