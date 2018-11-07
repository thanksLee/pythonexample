sports = {"축구" : "박지성", "야구": "강정호", "체조" : "손연제"}
print(sports["축구"])


aa = {1 : "안녕"}
aa[2] = "하이"

aa[3] = "방가"

aa[4] = [1, 2, 3]

aa[5] = 34

print(aa)

del aa[3]

print(aa)

print(aa.keys())

print("======= dict =============")
aa = dict()

print(aa)

aa["one"] = "첫번째"
print(aa)

bb = {"name": "홍길동", "hp": "010-1111-1111", "age":33}
keylist = bb.keys()
print(keylist)


for key in keylist:
    print(key)

keylist1 = list(bb.keys())
print(keylist1)


for key, value in bb.items():
    print("key : ", key, " - value : ", value)

# valueLit를 만드는 함수(values())
valueList = bb.values()
print(valueList)


# key와 value 한쌍(항목)을 열기 (items())

item = bb.items() # 리턴 값은 dict_items 객체이다.(key:value 의 쌍으로 구성)
print(item)

age = bb['age']
print(age)

try :
    agc = bb['afaasdfasdf'] # 키값 에러
    print(agc)
except:
    print("에러")

age = bb.get('age')
print(age)

gg = bb.get("asdfadsf")
print(gg)



gender = bb.get("gender", "디폴트")
print(gender)

# 딕셔너리에 해당 키가 존재하는지 알아보기
confirm_bb = "gender" in bb
print(confirm_bb)

confirm_bb = "age" in bb
print(confirm_bb)

# pop() 함수를 이용하여  value값을 가져오기

gg = bb.pop("name")
print(gg)
print(bb)

try:
    gg = bb.pop("adsfadfadf")
    print(gg)
except:
    print("오류 발생!!!")


gg = bb.pop("adsfadfadf", "pop sdfasdfasdf")
print(gg)


length = len(bb)
print(length)

bb.clear()
print(bb)