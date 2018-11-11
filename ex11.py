class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("{} 객체를 만드는 중".format(self.name))
    
    def speak(self):
        print("내 이름은 탐정 {} 나이는 {}".format(self.name, self.age))


per = Person("병훈", 30)
print(per.speak())


class Sutudent(Person):
    def __init__(self, name, age, hakbun):
        Person.__init__(self, name, age)
        self.hakbun = hakbun
        print("{} 학생을 만드는중...".format(self.name))

    def speak(self):
        Person.speak(self)
        print("나는 {:d} 학번입니다.".format(self.hakbun))


class Professor(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age)
        self.pay = pay
        print("{} 교수객체를 만드는 중..".format(self.name))
    
    def speak(self):
        Person.speak(self)
        print("페이가 {:d}인 교수".format(self.pay))

s = Sutudent("홍길동", 15, 201503030)

p = Professor("김교수", 33, 20000)

member = [s, p]
for aa in member:
    print(aa.speak())
