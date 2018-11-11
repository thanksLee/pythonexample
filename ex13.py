def sum(i, j):
    return i + j

def differ(i, j):
    return i - j

#print(sum(1, 3))

if __name__ == "__main__":  # prompt 상에서 ex13.py를 실행시에만 실행 (즉, import 할때는 실행되지 않는다.)
    print("sum : ", sum(1, 2))
    print("differ : ", differ(1, 3))