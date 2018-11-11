import sys # sys라고 하는 표준 라이브러리를 불러온다.
           # 이 모듈(sys 모듈)을 앞으로 사용할 것이다른ㄴ 것을 파이썬에게 알려주는 과정이다.

# sys 모듈은 파이썬 인터프리터와 인터프리터가 실행중인 환경(자신의 시스템)에 관련된 기능을 갖고 있다.
# 실행시 ex12.py thanksLee, Daniel, Julie

# 파이썬이 모듈을 찾는 과정
# 내장 모듈인 경우 파이썬은 이미 어디에 모듈이 있는지를 알고 있다.(쉽게 찾는다.)
# 내장 모듈이 아닌 경우(직접 만들거나, 남이 만들어 놓은 라이브러리들)에는 
# sys.path 변수에 정의된 디렉토리들을 검색한다.
# 이 디렉토리에서 해당 모듈을 찾게되면 모듈 내부에 있는 명령(함수, 클래스)들을 읽어오게 된다.
# 초기화 과정은 모듈을 불러올때 이루어진다.

print("명령줄 인수 체크하기!!!")

# sys.argv 변수는 문자열 리스트이다. 명령줄 인수들을 담고 있는 리스트이다.
for n in sys.argv:
    print(n)

print(sys.argv[0])

print("\n\n파이썬의 sys.path 디렉토리", sys.path)
print("\n\n파이썬의 sys.path 디렉토리", sys.path[0])


def show_info(name):
    print("이름 : ", name)

def math1(i, j):
    return i + j

def math2(i, j):
    res = 0
    if (i + j) == 0:
        print("제로 입니다.")
    else:
        res = (i + j)
    return res