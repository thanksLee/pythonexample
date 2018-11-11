class Person:
    def say(self):
        print("안녕, 친구야!!")


p1 = Person() # 객체화 과정 : 메모리에 객체를 생성한다.(instance화 한다.)

print(p1.say()) # self의 대입값을 전달하지 않았음에도 불구하고 에러가 없다. 즉 파이썬에서 자동으로 전달을 한다는 의미

class Person1:
    pass

p2 = Person1() # 객체화 과정 : 메모리에 객체를 생성한다.(instance화 한다.)
print(p2)


# init method
class Personal:
    def __init__(self, name):
        self.name = name
    
    def say(self):
        print("내이름은 ", self.name)

p1 = Personal("홍길동")

print(p1.say())

print("===================")
print("# 클래스 변수와 객체변수 예")
print("===================")

class Man:
    # 클래스 변수(Method 밖에 있는 변수)
    cnt = 0

    def __init__(self, name): # __init__ 은 생성자라고도 한다.
        # data 초기화
        self.name = name
        print("({} 이(가) 만들어지는 중)".format(self.name))

        Man.cnt += 1 # 클래스 변수 접근하기 : 클래스명, 클래스변수명

    def die(self):
        print("{} 는 죽었습니다.".format(self.name))

        Man.cnt -= 1

        if Man.cnt == 0:
            print("{} 는 최후의 생존자였다.".format(self.name))
        else:
            print("아직 {:d} 의 생존자가 남아있다.".format(Man.cnt))
    
    def say(self):
        print("생성 완료...안녕하세요!! 내 이름은 {} 입니다.".format(self.name))

    @classmethod #장식자(데코레이터) : 클래스, 함수를 포장한다.
    def how_many(how):
        # 현재의 객체 수량을 체크한다.
        print("현재 {} 명이 남았습니다.".format(Man.cnt))

        #how_many = classmethod(how_man) 이것이 생략

gameActor1 = Man("맨1")
gameActor1.say()
gameActor1.how_many()
gameActor2 = Man("맨2")
gameActor2.say()
gameActor2.how_many()

print("---------")
gameActor2.die()
Man.how_many() # 클래스 메소드 호출 방법 : 클래스명.메소드명