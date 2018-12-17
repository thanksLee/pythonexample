1. python 기초
```
- 주석표현으 '#'으로 표시한다.
- 자료형(DataType)
  > 프로그래밍을 할때 숫자, 문자열 등등의 것들을 뜻한다.
```

2. 자료형의 종류
```
- ex) ex01.py
- 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불린
  1) 숫자형
    > 정수 : 1234
    > 실수 : 123.59
    > 복소수 : 1+10!
    > 8진수 : 0o25
    > 10진수 : 0x2F
    - 크게 2가지로 분류하면
        > 정수형(Integer), 부동소수점(float)
    - 숫자연산
        > 사칙연산(+, -, *, /) 을 계산기와 마찬가지로 사용한다.
        > ** : 승 값을 나타내는 연산자
        > %  : 나머지값을 반환하는 연산자
        > // : 소수점 자리를 버리는 연산자
  2) 문자열
    > 문자의 나열을 의미한다.(문자들의 집합)
    > 작은 따옴표, 큰따옴표를 이용해서 문자열을 지정할 수 있다. 예) '헬로우 파이썬!'
      공백과 띄어쓰기 탭등이 그대로 유지된다.
    > 큰따옴표 : 작은 따옴표로 둘러싸인 문자열과 완전히 동일하게 취급된다.
      예) "Hello Python!" 큰따옴표 안에 작은 따옴표를 포함할 수 있다.
    > 세개의 따옴표 표현하는 경우 (""" 또는 ''')
    > 세게의 따옴표를 사용하는 경우는 여러 라인에 걸친 문자열을 표현할때 사용한다.
    > 한글 깨짐
      * # -*- coding: utf-8 -*-, u'한글깨짐' 으로 처리
    > escape code
      * \n : 개행(줄바꿈)
      * \r : 캐리지리턴
      * \" : 큰 따옴표 출력(")
      * \' : 작은 따옴표 출력(')
      * \000 : 널문자
      * \t : 수평탭
      * \\ : '\' 문자표현 ('\')
    - 문자열 연산
        > 파이썬에서는 문자열을 더하고 곱할수도 있다.
      * 문자열 더하기 (concatenation) : 문자열 + 문자열
      * 문자열 곱하기 : 문자열의 반복을 의미한다.
                       문자열 * 숫자는 문자열을 숫자만큼 반복을 의미한다.
      * 문자열의 인덱싱과 슬라이싱
    > 문자열 포멧(format) : 문자열 내에 어떤 특정 값을 변화시키는 방법
      예) 현재 날짜는 6월 20일이다.
         하루후,
            현재 날짜는 6월 21일 입니다.

      %s : 문자열(String)
      %d : 정수(Integer)
      %f : 실수형(float)
      %c : 문자(character)
      %o : 8진수
      %x : 16진수
      %% : 리터럴 %
  3) 리스트 (list)
    > 다른 언어의 배열과 같은 형을 의미한다.
    > 리스트 내에는 어떠한 자료형도 포함시킬수 있다.
  4) 튜플(tuple) : 리스트와 비슷한 자료형이다.
    > 리스트, 튜플의 차이점
      * 리스트는 [], 튜플은 () 를 사용한다.
      * 리스트는 요소의 변경(수정, 삭제, 생성)이 가능하지만, 튜플은 요소의 값을 변경할 수 없다.

    사용예)
    tu = () --> 빈값이 들어 있는 형태
    tu2 = (1,)
    tu3 = (10, 20, 30, 40)
    tu4 = 10, 20, 30
    tu5 = ("국제시장", "명량", ("ab", "cd"))
  5) 불린형 (참과 거짓)
    > 문자열 : "aaa" --> 참(true), 거짓(false)
    > 리스트 : [1, 22, 33] 참, [] (거짓)
    > 튜플   : ('a', 'b') 참, () 거짓
    > 딕셔너리 : {} 거짓
    > 숫자 : 1(참), 0(거짓)
    > None : 거짓
```
3. 변수 (Variable)
```
- ex) ex02.py
- 변수는 객체를 가리키고 있는 것이다.(참조한다.)
- 'is' 라는 (파이썬의 내장 함수)를 이용해서 두개의 변수가 서로 같은 값을 갖고 있는지 파악할 수 있다.
- 식별자 만들기
  > 식별자의 첫 문자는 알파벳문자, 밑줄이 와야 한다.
  > 첫문자 이외의 나머지 글자는 밑줄, 숫자(0~9)가 올 수 있다.
  > 식별자는 대/소문자를 구분한다.
     ex) myname과 myName은 서로 다르다.
  > 식별자는 공백이 들어가면 안된다.
     ex) i, aa, name_1_2(올바른 식별자) 2name, a a b b, my-name, ?abc (잘못된 식별자)
```

4. 제어문
```
- ex) ex03.py
- 조건문, 반복문 : 프로그램의 흐름을 효율적으로 제어를 해서 효율적으로 이용하기 위한 명령문
- 조건문 : if문
  > if문의 기본 구조

    if <조건문>:
       <실행할 문장>
       <실행할 문장>
    elif <조건문>
       <실행할 문장>
       <실행할 문장>
    else :
       <실행할 문장>
       <실행할 문장>

  > indentation(들여쓰기)
    : if문을 작성할때 들여쓰기를 해야 한다.
  > if <조건문> 다음에 반드시 ":" 와야 한다.
  > 일반적으로 파이썬에서는 문장 끝에 ';' 생략하고 사용한다.
- 비교연산자
  >   < : X < y ---- x는 y보다 작다
  >   > : x > y ---- y는 x보다 크다
  >   == : x == y ---- x와 y는 같다
  >   !=  :  x != y --- x와 y는 서로 다르다
  >   >= : x >= y ----- x는 y보다 크거나 같다.
  >   <= : x <= y ---- x는 y보다 작거나 같다.
- 논리 연산자 (and, or, not)
  > x and y : x와 y가 모두 참일때 참
  > x or y : x와 y 둘중에 하나만 참일때 참
  > not x : x가 참이면 거짓
- in 연산자
  > x in 리스트, x not in 리스트, x in 튜플, x not in 튜플, x in 문자열, x not in 문자열

- 반복문 : while, for 문
```
5. 반복문
```
- ex) ex04.py
- while 문의 구조
  > while <조건문> :
      <실행할 명령문 1>
      <실행할 명령문 2>
      <실행할 명령문 3>
  > while 1:
      <실행할 명령문 1>
      <실행할 명령문 2>
- 보조 제어문 (break, continue)
- for 문의 구조
  > for 변수 in 리스트(튜플, 문자열):
      <실행할 명령문 1>
      <실행할 명령문 2>
    else:
       여기서 else는 루프를 다 돌고 난뒤에 항상 수행한다.
       단. Break를 이용해서 빠져나오면 실행되지 않는다.
- for 문과 range 함수
  > range 함수는 두개의 숫자를 이용하는 함수이다.
    숫자가 두개인 경우 1씩 증가하는 숫자의 리스트를 반한한다.
    숫자가 세개인 경우 세번째 숫자는 증가치를 의미한다.
  > 사용 예
    range(1,5) -> 리스트[1, 2, 3, 4] 반환한다.
    range(1, 5, 2) -> [1, 3]

    주의 : 두번째 숫자 이하가 아니라 미만까지만 반환을 한다.
- 리스트 내포(List Comprehension)의 기보적인 구조
  > [표현식 for 항목 반복 가능한 객체 if 조건위에서 if 조건은 생략이 가능하다.]
  > [표현식 for 항목1 in 반복가능한 객체1 if 조건1
                항목2 in 반복가능한 객체2 if 조건2
                ...
                항목n in 반복가능한 객체n if 조건n
   ]
```
6. 함수
```
- ex) ex05.py
- 재사용 가능한 프로그램, 명령 덩어리
- 함수는 프로그램을 작성할 때 필요한 중요한 단위이다.
- 함수는 내장함수, 사용자 함수가 있다.
- 함수르 사용하는 이유는 사용하기 편하게 하기 위해서 이다.
- 리스트 함수들
  > 문자열과 같이 리스트 변수명 뒤에 .함수명을 연결하여 사용한다.
```
7. 사용자 정의 함수
```
- ex) ex06.py
- def (define) 함수명():
    <실행할 명령1>
    <실행할 명령2>
    ...
    인수(매개변수, 파라메터)
- 예상할수 없는 인수를 갖는 함수 (동적 파라메터)
  def 함수명(*인수), def 함수명ㅁ(key, val)
- 리턴값의 유형
  > 두개의 값을 리턴 할수 있다. (튜플형태로..)
  > return 만 단독으로 사용할 경우에는 함수를 바로 빠져나간다.
- 인수에 초기값을 설정하기
  > 인수 초기화는 인수 선언의 제일 마지막에 처리
```
8. 파일입출력
```
- ex) ex07.py
- 파일 생성
  > 파일 객체 = open(파일이름, 파일 열기모드)
    -- 파일 열기 모드 --
    * r 모드 : 읽기 모드 - 파일을 읽기 용도로 사용할때
    * w 모드 : 쓰기모드 - 파일에 내용을 쓸때(쓰기모드로 열때 원래 있던 내용이 모두 지워지고 열린다.)
                       - 파일이 존재하지 않을 경우에는 새로운 파일이 생성된다.
    * a 모드 : 추가 모드 - 파일에 새로운 내용을 추가 할때.
  > 파일을 open했으면 close를 해야한다. 하지만 명시적으로 close를 하지 않아도 된다.
    파이썬은 프로그램 종료시 열린 파일을 객체들을 자동으로 닫아준다.
    쓰기 모드로 열었던 파일을 닫지 않고 재사용하는 경우에는 에러가 발생하기 때문에 닫아주는 습관을 갖자.
- 파일을 읽어오는 방법
  > readline() : 파일 객체에서 사용할 수 있는 readline() 이용하기
    * 더이상 파일에서 읽어올 라인이 없을 경우 None
  > readlines() : 리스트로 리턴
  > read() : 파일 내용 전체를 문자열 형태로 리턴
- a(append) 모드를 이용해서 파일에 내용을 추가하기
- with문을 이용해서 파일 객체 다루기
  > with문을 이용하면 파일을 닫을 필요가 없다.
  > 자동으로 파일을 닫아준다.
  > 파일을 오픈하여 제일 마지막까지 읽었으므로 다시 읽으려면 포인터를 제일 처음으로
    읽으려면 seek() 함수를 이용하자
- import를 이용한 모듈 입력 방법 (모듈 : 함수들과 변수들을 모아놓은것)
  > sys 모듈은 내장 모듈
```
9. 딕셔너리
```
- ex)ex08.py
- 키값을 이용하여 값을 가져온다.
- 주의 사항
  > key값(지수)은 고유한 값이므로 중복되는 값을 설정해 놓으면 안된다.
    만약 중ㅂ고이 된다면 하나만 적용되고 나머지는 제외된다
  > 키값으로 리스트는 쓸수 없다. 튜플은 키 값으로 사용가능하다.
  > 키값이 변할 수 없다는 전제하에 타입을 설정하면 된다.
- dict() 함수
  > 이 내장함수는 항목(key:value)이 없는 딕셔너리를 만든다.
- key 리스트를 만드는 함수  : keys
- value 리스트를 만드는 함수 : values
- key와 value 한쌍(항목)을 얻기(items())
  > 리턴 값은 dict_items 객체이다.
    이 객체의 요소는 튜플로 구성된다. {key : value}
- key:value 쌍을 모두 삭제하기 clear()
- 특정 key삭제 (del aa[3])
- 특정값 가져오기 : bb.get("age")
  key 값이 없다면 None를 리턴
- 딕셔너리내에 키값이 없을 경우 디폴트 값을 주는 방법
  > get("gender", "default값")
- pop() 함수를 이용하여  value값을 가져오기
  > 가져온 값을 원래의 값에서 제거한후 가져온다.(copy, cut 중에 cut)
  > 키값이 없다면 오류 발생
  > default 값을 설정 할 수 있다.
- 딕셔너리의 항목 갯수를 구함
  length를 활용
```
10. set
```
- ex) ex09.py
- 집합에 관련된 것들을 쉽게 처리하기 위한 자료형 'set' 키워드를 이용하여 만들수 있다.
- 집합의 특징 : - 중복을 허용하지 않는다.(중복을 제거하기 위한 필터로 활용되기도 한다.) - 순서가 없다.
- 리스트 튜플은 순서가 있다. 따라서, 인덱싱을 이용하여 값을 얻을 수 있다.
- 집합은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
  딕셔너리 역시 순서가 없는 자료형이다.
- 집합과 딕셔너리는 인덱싱을 지원하지 않는다.
- 집합에 저장된 값을 인덱싱으로 접근하기 위해서는 리스트나 튜플로 변환해야 한다.
- 교집합, 합집합, 차집합을 이용하자.
- 대칭 차집합(^) : 두개의 집합이 있을때 둘 중 한 집합에만 있는 항목들
```
11. 클래스

- 클래스의 기초
```
- 클래스 선언

class Test: # 클래스명은 첫글자는 대문자로 사용한다.
    str = "클래스 잡기"  # str은 Test 클래스의 요소(attribute, field) 또는 Test클래스의 멤버라고도 한다.

test1 = Test() # test1 객체는Test 클래스에 의해서 만들어진 인스턴스, test1은 Test클래스의 인스턴스
               # Test는 붕어빵 틀이고, test1은 붕어빵과 같다.

print(test1.str)
```
-클래스의 구성
```
- ex) ex10.py
- Class 클래스명 :
  > 변수 : 클래스에 소속된 변수들을 필드(field)라고 부른다.
  > 함수 : 이러한 함수들을 클래스의 메소드(method)라고 한다.
  > 결론적으로 클래스는 필드와 메소드로 구성된다.
    변수나 함수와는 다르게 구별지어서 부르는 것은 클래스나 객체에
    소속되어 있는대상이라는 것을 나타내기 위함이다.
  > 필드와 메소드 들을 통틀어 클래스의 속성(attribute)이라고 부른다.
  > 클래스내의 메소스와 일반 함수와의 차이는 바로 'self' 다.
  > 메소드의 경우 매개 변수의 목록에 항상 추가로 한개의 변수(self)를 맨앞에 추가해야 한다.
    꼭 self를 사용해야 하는 것은 아니지만, 일반적으로 self를 사용한다.
    (self[자기자신]를 표준으로 사용하고 있다.)
    메소드를 호출 할때 이변수(self)에 직접 값을 넘겨주지 않는다.
    파이썬이 자동으로 self에 값을 할당한다.
    self는 c++에서의 this pointer와 같은것, java, c#에서는 this 참조변수.
  > 필드는 일반적으로 변수와 똑같다.
    한가지 차이점이 있다면 네임스페이스에 묶여 있다라는 점이다.
    필드는 해당 클래스 또는 객체 내부에서만 의미가 있다.
    해당 클래스 내부와 객체 내부를 네임스페이스라고 한다.
    다시 얘기해서 필드가 통용되는 공간(필드 내부, 객체 내부)를 의미한다.
  > 필드에는 클래스 변수가 있고, 객체변수가 있다.
    (필드를 소유하고 있는 대상이 클래스이냐, 객체이냐에 따라서 클래스변수, 객체변수로 구별된다.)
  > 클래스 변수는 공유된다.(다시 얘기해서, 클래스로부터 생성된 모든 인스턴스들이 접근 할 수 있다.)
  > 클래스 변수는 하나만 존재한다. 어떤 객체가 클래스 변수를 변경한다면 다른 인스턴스들에게도 변경 내용이 반영된다.
  > 객체변수(인스턴스변수)는 클래스로부터 생성된 각각의 객체(인스턴스)에 속해있는 변수
```
- init 메소드
```
- ex) ex10.py
- 파이썬 클래스는 여러가지 특별한 메소드가 존재한다.
  그 중에서 init 메소드는 클래스가 인스턴스화(객체화)될때 호출된다.
- 객체가 생성될때, 여러가지 초기화작업을 할때 유용하게 사용할 수 있다.
  메소드명은 '__init__' 이다.
```
12. 상속 : 재사용의 한가지 방법
```
- ex) ex11.py
- 객체지향의 가장 큰 장점은 코드의 재사용(재활용).
```
13. 모듈
```
- ex) ex12.py, ex13.py, ex14.py
- 함수, 변수, 클래스들을 모아놓은 파일
- 모듈은 다른 파이썬 플그램에서 불러서 사용할 수 있게끔 만들어진 파이썬 파일을 말한다.
- 모듈을 만드는 방법 : *.py 확장자를 이용하여 직접 만들 수 있다.

- 다른 사람들에 의해서 만들어진 파이썬 라이브러리들을 모듈이라 한다.
- 모듈을 불러오는 방법 : import 명령을 통해서 모듈을 불러와 사용할 수 있다.
- 파이썬에서 제공하는 표준 라이브러리도 모듈이다. 표준라이브러리도 import를 이용하여 불러온다.
- 파이썬 프로그래밍시에 많은 모듈을 사용한다.
- 사용자 정의 모듈
- from 모듈 이름 import 모듈함수1, 모듈함수2, ...
  from ~ import 문을 이용하면 모듈 이름을 붙이지 않고 바로 해당 모듈 함수 사용 가능.
  , (콤마)를 사용하지 않고 여러 함수를 불러올 수 있는 방법
  from 모듈이름 import *
- 바이트코드 형태의(컴파일된 파일) .pyc 파일
  > 파이썬에서는 모듈을 불러올때 좀더 빠르게 처리 할 수 있도록 하기 위해서 .pyc 확장자를 가지는 바이트 코드를 활용한다.
  > 파이썬에서 컴파일 할때 만들어 놓은 파일이다. 모듈을 불러올때는 .pyc 파일을 이용하여 불러오게한다.
  (불러올때 선행작업을 수행하지 않고, 더 발리 모듈을 불러올수 있다. 이러한 바이트코드는 플랫폼에 구애받지 않고 사용가능.)
  > 참고로, 파이썬이 저장 디렉토리에 쓰기 권한이 없을 경우에는 생성되지 않는다.
- 모듈의 name속성 (__name__)
  모든 모듈은 이름을 갖고 있다.
  > 모듈의 name 속성을 이용하면, 외부로부터 불러들여 졌을때, 곧바로 실행되지 않게 할 수 있다.
  > 파이썬의 모듈은 name 속성을 가지고 있는데 name이 'main'일 경우에는 사용자가 직접 실행한 것임을 의미한다. 따라서 적절하게 name속성을 활용하여 요구에 맞게 실행될 수 있도록 한다.
- dir() 내장 함수
  > 개체에 정의 되어 있는 식별자들을 알려주는 함수
  > 리스트 형태로 반환하는 함수
  > from 모듈 import로 했을때는 dir(모듈) 은 안되고, import 모듈 dir(모듈)은 된다.
- 패키지 : 단순하게 폴더라고 생각하자
  > 파이썬에서 폴더는 모듈을 담는 역할을 한다. init.py 파일 포함
```
14. 패키지 만들기
```
- 디렉토리 구조
  python
    - aaa
       - bbb
          - ccc
```
15. 예외처리
```
- ex) ex15.py
- 예외 : 프로그램에서 벌어지는 예외적인 상황을 의미
         ex) 파일을 읽고자 할때 그 파일이 존재하지 않을 경우
             프로그램이 한창 실행 중일때 갑자기 그 파일이 지워진 경우

             이러한 예외 상황을 처리해주는 것을 예외처리라고 한다.
- 에러의 예
  > FileNotFoundError(파일이 없을때)
  > ZeroDivisionError(숫자를 0으로 나누었을때)
  > IndexError(리스트에서 얻어 올수 없는 값일 경우)
  > SyntaxError(구문 오륜)
  > EOFError (파링의 끝일 경우:읽을 내용이 없을때)

  파이썬은 오류 발생시 프로그램을 중단하고 에러 메시지를 보여준다.

- 예외 처리 기본 형식(자바의 try~catch문)
  try:
    수행명령..
  except [발생에러 [as 에러메시지 변수]]: <- 는 생략이 가능하다.
    수행명령..
  except:  [발생에러 [as 에러메시지 변수]]:
    수행명령
  else:
    수행명령

- try ~ finally
  > try 문 수행도중에 예외상황 발생여부 관계없이 항상 수행된다.
- 에러 피하기(pass 활용)
  > 특정 에러가 발생할 경우 통과시키는 방법
- 예외 발생시키기
  > raise 명령어를 이용해서 에러를 강제로 발생시키는 방법
- 사용자 정의 예외 만들어서 발생시키기
  > 에러(오류)나 예외는 반드시 직간접적으로 Exception 클래스에서 파생된 클래스이어야 한다
```
16. ETC
```
- ex) ex15.py, ex16.py
- lambda : 함수를 생성할때 사용하는 예약어 def와 동일한 기능의 예약어이다.
          보통 한줄로 간결하게 함수를 만들어 사용할때 사용한다.
          def를 사용할 수 없는 곳에서 사용한다.
          익명함수라고도 한다.
- 사용형식
  > lambda 인수1, 인수2, ... : 인수 결과
```
17. Library
```
- ex) ex16.py, ex17.py, ex18.py
- 전세계의 파이썬 개발자(사용자)들에 의해서 이미 만들어진 프로그램들을 모아놓은 것을 말한다.
- 파이썬 설치시에 자동으로 컴퓨ㅓ에 설치가 된다.
- sys모듈, pickle 모듈, I/O 모듈, OS 모듈, glob 모듈, time 모듈, calendar 모듈, random 모듈, thread 모듈
- sys.argv : dos command 상에서 선언된 parameter를 리스트 형태로 돌려준다.
- sys.exit() : 중간에 바로 종료 : ctrl + z, ctrl + d 를 눌러서 대화형 인터프리터를 종료하는 기능
- sys.path : 자신이 만든 모듈을 불럿 사용하기 위해서 위치를 지정하는 명령
- pickle 모듈 : 객체 형태를 그대로 유지해서 파일에 저장시키고, 불러올 수 있게 하는 모듈.
              바이너리 형태로 저장한다.
  > pickle을 이용해서 파일에 저장 및 조회할 때는 꼭 바이너리 처리를 해야 한다.
    b를 입력해서 바이너리라는 것을 표시해야 한다.
  > 바이너리라는 것을 표시해야 한다.
  > 저장시 picke.dump(objec, file), 불러올때는 pickle.load(file)
  > pickle.dumps(object) ----> String,
    pickle.loads(String) ----> Object
- os 모듈
  > os.environ : 시스템의 환경변수값 들을 보여주는 역할을 한다.
                시스템의 정보를 딕셔너리 객체로 돌려준다.
  > os.chdir : 현재 디렉토리의 위치를 변경하는 함수
  > os.getcwd : 자신의 디렉토리의 위치를 알려준다.
  > os.system("명령어") : 시스템의 유틸리티나 dos 명령어들을 파이썬에서 호출한다.
  > os.popen : 시스템 명령어를 시킨 결과값을 읽기 모드의 파일 객체로 돌려준다.
  > 기타 os 모듈의 유용한 함수들
    * os.mkdir(디렉토리명) : 디렉토리를 생성한다.
    * os.rmdir(디렉토리명) : 디렉토리를 삭제한다. (디렉토리가 비어있어야 한다.)
    * os.rename(src, dst) : src 이름의 파일을 dst 이름으로 변경
- shutil : 파일을 복사해주는 모듈
  > shutil.copy(src, dst)
  >  src 이름으로
- glob 모듈
  > 디렉토리에 있는 파일들을 리스트로 만들때 사용한다.

- 임시파일(tmpfile) 모듈
  > 임시적으로 파일을 만들어서 사용할때 유용하게 쓰이는 모듈이다.
  > tempfile.mktemp() : 임시로 파일을 만들어서 돌려주는 함수(중복되지 않도록 만들어준다.)
  > tempfile.TemporaryFile() : 임시적인 저장 공간으로 사용될 파일 객체를 도려주는 함수
    w+b 모드를 갖는다.
  > mode
    * w : 쓰기 모드로 파일 열기
    * r : 읽기 모드로 파일 열기
    * a : 추가 모드로 파일 열기
    * b : 바이너리 모드로 파일 열기
      w+, r+, a+ 파일을 업데잍 할 용도로 사용
      b는 w, r, a 뒤에 붙여서 사용한다.

      r : 단지 읽기 위해서 사용하는 모드, 포인터 위치는 파일 처음에 위치한다.
      r+ : 읽기와 쓰기 모드로 파일을 연다. 포인터 위치는 파일 처음에 위치한다.

      w : 파일을 쓰기 모드로 열고, 파일이 없는 경우에는 새로 만든다.
          포인터 위치는 파일 처음에 위치한다.
      w+ : 읽기와 쓰기 모드로 열고, 파일이 없을 경우에는 새로 만든다.
          포인터 위치는 파일 처음에 위치한다.

      a : 쓰기모드로 파일을 열고, 파일이 없는 경우에는 새로 만든다.
          포인터 위치는 파일의 끝에 위치한다.
      a+ : 읽기와 쓰기 모드로 파일을 연다. 파일이 존재하지 않을 경우에는 파일을 생성한다.
           포인터 위치는 파일의 끝에 위치한다.

      모드활용예 >>>
      파일 읽으려면         --> r, r+, w+, a+
      파일을 쓰려면         --> r+, w, w+, a, a+
      없는 파일을 생성하려면 --> w, w+, a, a+
      파일을 덮어쓰려면      --> w, w+
      파일을 덧붙이려면      --> 앞쪽에 붙이려면 :  r+
                                뒷쪽에 붙이려면 : a, a+

- time 모듈
  > 시간과 관련된 것들(유용한 시간 함수들을 많이 가지고 있다.)
    * time.time() : 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려주는 함수
                    UTC(Universal Time Coordinated 세계 협정 표준시)를 이용해서 실수 형태로 반환한다.
    * time.localtime : time.time() 를 통해서 얻어온 실수값을 이용해서 년도 월, 일 시 분초의 형태로 바꾸어주는 함수이다.
    * struct_time 객체 속성
        tm_year : 년도
        tmp_mon : 월(1~12)
        tm_mday : 일
        tm_hour : 시간 (0~23)
        tm_min  : 분
        tm_sec  : 초
        tm_wday : 요일을 숫자로 표현(월요일 : 0 ~ 일요일 : 6)
        tm_yday : 1월 1일 부터 누적된 날짜를 나타냄(1~366)
        tm_isdst : 서머타임(일광절약 시간제 : 0, 1, -1)

    * time.gmtime : UTC 기준의 현재시간
    * time.asctime : 알아보기 쉬운 날짜와 시간을 반환해주는 함수
    * time.ctime : time.asctime을 더 간단하게 표시하는 함수
    * time.strftime : 시간을 나타내는 포맷을 지정해서 세밀하게 표현할 수 있는 함수
        형식 지정자 (포멧코드)
        %y 년도 축약 (2015 --> 15), %Y(2015)
        %a 요일 축약 (Sun, Sat, Mon..), %A(Sunday, Saturday..)
        %b 월축약 (Jan), %B(January)
        %c 날짜와 시간을 출력(15/01/01 13:21:10)
        %d 날(day) --> 01 ~ 31
        %H 시간을 24시간 ---> 0 ~ 23
        %I 시간을 12시간 ---> 01 ~ 12
        %j 누적 날짜 표현 --> 001 ~ 366
        %m 달 ---> 01 ~ 12
        %M 분 ---> 01 ~ 59s
        %p 오전/오후 ---> AM, PM
        %S 초 --> 00 ~ 61
        %U 누적주 --> 일요일 시작 00~53
        %w 요일 --> 0 ~ 6
        %W 누적주 --> 월요일 시작 00 ~ 53
        %x 날짜 출력 ---> 15/01
        %X 시간 출려 ---> 13:12:12
        %Z 시간대 출력 --> 대한민국 표준시
    * time.sleep : 루프문 안에서 많이 사용된다. 일정한 시간 가격을 주기위해서 사용하는 함수이다.

- calendar(달력) 모듈 : 파이썬에서 달력을 표시해주는 모듈이다.
  > calendar.calendar(해당연도) : 해당년도의 전체 달력을 출력
  > calendar.prcal(해당연도) : 해당 년도의 저체 달력을 출력
  > calendar.prmonth(년도, 월) : 해당년도의 월만 출력해준다.
  > calendar.weekday(년도, 월, 일) : 입력받은 날짜의 요일을 반환한다.
  > calendar.monthrange(년도, 월) : 입력받은 월의 1일이 무슨 요일인지와 그달의 마지막 일자를 반환해주는 함수

- random 모듈
  > 난수 발생 모듈
  > 난수 : 0.0 ~ 1.0 사이의 실수 값

- pprint(pretty printer) : 자료구조를 사람이 보기좋게 출력하는 모듈
  > pprint모듈에 pprint() 함수를 이용하여 자료구조를 출력해 보기
  > 복잡한 구조를 좀더 보기 좋게 표현
```
18. 파이썬에서 제공하는 표준 자료 구조
```
- 참조 사이트 : docs.python.org/3/libary
- ex) ex19.py, ex20.py, ex21.py, ex22.py, ex24.py
- 리스트, 튜플, 딕셔너리(사전), 셋(집합)
  > collections 모듈
    * deque(양쪽이 열려있는 큐구조), defaultdict, Counter, namedtuple,
      # Deque = 양방향 큐(데크)는 컨테이너 양쪽 (앞뒤)에 아이템을 넣거나 뺄수 있다.
    orderedDict
      # Counter : 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
      # Counter 객체는 산술/집합 연산이 가능하다.
      # defaultdict 메서드는 컨테이너를 초기화 만들때 default 값을 지정한다.
  > array 모듈
    * array 사용하는 방법
    * sequence 자룍조를 정의하는데, list와의 차이점은 모든 자료형이 동일해야 한다.
    * 참조 : https://docs.python.org/3/library/array.html
    * array 의 내용을 파일에 쓰거나 읽기
  > heapq 모듈 (힙생성, 힙내부자료 접근)
    * heap 이란 자식노드가 부모노드와 정렬관계를 가지는 트리형 자료 구조
    * 이진힙의 경우 array나 list를 사용해서 표현할 수 있다. (인덱스를 이용해서 표시할 수 있다.)
    * Heap은 최대 힙 (max-heap : 부모가 자식보다 크거나 같다)
             최소 힙 (min-heap : 부모가 자식과 같거나 작다) 이 있다.
            max-heap : 위로갈수록 커지는 형태
            min-heap : 아래로 갈수록 커지는 형태
    * 파이썬의 heapq모듈은 최소힙(min-heap) 으로 구현된모듈이다.
    * 힙생성 : heappush() : 한개씩 가져와서 정렬, heapify() : 메모리 파일에서 정렬
               heapify()가 성능이 더 좋다.
    * heap data 접근 : heappop()을 이용하여 가장 작은 값을 하나씩 끄집어 낸다.
    * heap data 교체 : heapreplace()
    * 힙의 최대/최소 값 구하기 : nlargest(), nsmallest()
    * 리스트의 개수가 적을때 유리, 많으면 불리
  > bisect 모듈(정렬된 상태로 요소를 추가, 중복값 처리)
    * 정렬된 상태로 아이템(데이터)를 추가할 수 있는 모듈
      데이터가 많은 리스트를 사용할 경우 힙방식보다 시간과 메모리 낭비를 줄일 수 있다.
    * insort 는 오른쪽에서 정렬(insort = insort_right)
  > queue
    * FIFO : First In First Out
    * LIFO : Last In First Out (Stack)
    * PUT : 데이터 삽입
    * GET : 데이터 가져오기
    * 우선 순위 큐 구현 (우선순위에 따라 아이켐을 정렬하고, 우선순위가 가장 높은 아이템을 팝하는 큐를 의미)
    * queue.PriorityQueue 이 클래스를 이용하면 우선순위 큐를 구현가능 (쓰레드의 개념을 익힌후 사용)
    * heapq 모듈을 응용해서 우선순위를 큐에 구현한다.
  > deque (ex24.py)
    * 자료구조 응용
      - Deque를 이용해서 고정크기의 큐를 생성하기 (maxlen = n)
      - maxlen의 크기보다 더 입력을 하면 마지막을 기준으로 없애도 새로 추가

  > struct
  > copy
  > generator / yield
    * yield의 리턴값이 generator object
    * yield는 generator 생성을 하고 generator는 next() 함수를 가지고 있다.
```
19. unpacking
```
- 예제) ex23.py
```
20. Dictionary
```
- 예) ex25.py
- dictionary key를 여러값에 매핑하기 (collections.defaultdict)
- dictionary에서 최대/최소/정령
  > zip() 함수를 이요해서 키(key) 와 값(value)를 뒤집는다.
  > 한번 zip() 함수를 이용하고 다시 이용하려면 set을 다시 해줘야 한다.
```