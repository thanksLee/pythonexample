aa = {"name":"홍길동", "id":"test", "email":"abab@naver.com"}
bb = {'order':'김말똥', 'tel':'010-0000-3242', "email":"bsct@naver.com"}

from collections import ChainMap

chain = ChainMap(aa, bb)

print(chain["order"] )
print(chain["name"] )
print(chain["email"]) # 키가 일치할때는 첫번째에서 찾고 없으면 그 다음 dict에서 찾는다.

print(len(chain)) # 키에 대한 length를 구한다.

print(list(chain.keys()))
print(list(chain.values()))

del chain['name']
print(list(chain.values()))

chain['pw'] = 1234
print(list(chain.values()))
print()
print()

chain['email']="test123@naver.com"

print(list(chain.values()))
print(aa)
print(bb)

print()

chain['order'] = "강길동"
print(list(chain.values()))
print(aa)
print(bb)
print()
print()

chain['order'] = "강길동1"
print(list(chain.values()))
print(aa)
print(bb)

# 아래 내용은 첫번째 매핑 데이터에 없는 키를 삭제하려면 오류가 발생
#del chain["tel"]

print('#######################')

aa = {"name":"홍길동", "id":"test", "email":"abab@naver.com"}
bb = {'order':'김말똥', 'tel':'010-0000-3242', "email":"bsct@naver.com"}

merge = dict(bb)
merge.update(aa)

print(merge['name'])
print(merge['order'])
print(merge['email'])