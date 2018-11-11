# 클래스, 변수, 함수를 포함하는 모듈 만들기


PI = 3.14192

class Math:
    def aaa(self, r):
        return PI * (r**2)
    
    def sum(self, i, j):
        return i + j


if __name__ == "__main__":
    print(PI)
    bb = Math()
    print(bb.aaa(10))
    print(bb.sum(PI, 10))


print("-------------------")
print("dir() 함수")
print("-------------------")


