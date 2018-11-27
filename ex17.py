import pickle

listA = ["a", "b", "c"]

fp = open("list.txt", "wb")

pickle.dump(listA, fp)

fp.close()

fp = open("list.txt", "rb")

listB = pickle.load(fp)

print(listB)

print(listB == listA)

fp = open("dic.txt", "wb")
data = {1:"hello", 2:"love"}
fp = open("dic.txt", "wb")
pickle.dump(data, fp)
fp.close()

fp = open("dic.txt", "rb")
data1 = pickle.load(fp)
print(data1)

class Foo:
    var = "Fool 클래스"

fooStr = pickle.dumps(Foo())

print(fooStr)

pickle.loads(fooStr)
print(Foo.var)

import os
print(os.environ)
print(os.environ["APPDATA"])

os.environ["추가"] = "adfadfadsf"
print(os.environ)

# dos 명령어 실행

print("현재 경로 : ", os.getcwd())

print("dir : ", os.system("dir"))
print("dir : ", os.system("dir/w"))


# shutil
import shutil

shutil.copy("src.txt", "dst.txt")

#glob
import glob

print(os.getcwd())

aaa = glob.glob(os.getcwd() + '\\e*')

print(aaa)