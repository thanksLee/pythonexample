# -*- coding: utf-8 -*-

aa = 100
bb = 100
cc = 100

print (aa is bb)

#변수 삭제하기
del(aa)

# 변수 선언 및 초기화
cc = 100
dd = 100

cc = dd = 100

print(dd)

cc, dd = "국제시장", "명량"

print(dd)

[cc, dd] = ["하이", "파이썬"]

print(cc)


print("---- 참조변수 혼동하기 쉬운 예 ----")
aa = ["a", "b", "c", "d", "e"]

bb = aa

print(bb)

aa[2] = "z"

print(aa)
print(bb)

print ("")
print("")
print("------ 데이터의 복사 ----------")
print("")

aa = ["a", "b", "c", "d"]
bb = aa[:] # aa의 리스트를 처음부터 끝까지 슬라이싱
aa[2] = "z"

print(aa)
print(bb)


