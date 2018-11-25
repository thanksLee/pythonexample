

try:
    fp = open("dkvlf", "r")
except:
    print("오류")

sss = input("숫자를 입력하세요..")

try:
    str = input("문자를 입력하세요. >>")
except EOFError:
    print("읽을 내용이 없습니다.")
except KeyboardInterrupt:
    print("입력 취소 되었습니다.")
else:
    print("당신이 입력한 문자는 ~~ {}".format(str))
finally:
    print("finally")


try:
    fp = open("nfile.txt")
except FileNotFoundError:
    pass # 파일이 없어도 예외로 처리하지 않고 넘어간다.

print("에러없이 수행됩니다.")


class Fleight:
    def fly(self):
        raise NotImplementedError #파이썬 내장에러 (interface가 구현되지 않았을때 발생키는 에러)


class Plane(Fleight):
    #pass
    def fly(self):
        print("빠른 속도로 날아가는 비행기 입니다.")

plane = Plane()
plane.fly()

class UserException(Exception): # 사용자가 정의하는 예외클래스
    def __init__(self, length, min_length):
        Exception.__init__(self)
        self.length = length
        self.min_length = min_length
    
try:
    txt = input("입력 내용 ==> ")
    if len(txt) < 5:
        raise UserException(len(txt), 5)
except EOFError:
    print("읽을 내용이 없습니다.")
except UserException as uex:
    print("UserException : 입력된 내용은 문장열의 길이가 {0} 입니다. " + \
            "최소한 길이가 {1} 이어야 합니다.".format(uex.length, uex.min_length)
            )
else:
    print("예왜 상황이 발생하지 않았습니다.")

print("-----------------------------------")
print("실저 테스트")
print("-----------------------------------")

import sys, time
fp = None

try:
    fp = open("test.txt", encoding="utf-8")
    while True:
        line = fp.readline()
        if len(line) == 0:
            break
        print(line)
        sys.stdout.flush() # print문 뒤에 사용해서 바로바로 화면에 출력하라
        time.sleep(2)
except IOError:
    print("읽을 파일이 없습니다.")
except KeyboardInterrupt:
    print("사용자가 취소를 하였습니다.")
finally:
    if fp:
        fp.close()
    print("파일 Close를 했습니다.")       

def map_test(li):
    res = []
    for i in li:
        res.append(i*3)
    return res


res = map_test([10, 20, 30, 40])
print(res)



#print(list(map(map_test, [10, 20, 30])))
sss = lambda x, y : x*y

print (sss(10, 20))
