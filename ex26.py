aa = [1, 2, 5, 11, 3, 6, 7, 10]

saa = aa[3:6]

record = "김말똥241994432424서울시"

print(record[5:9])

birth_year = slice(5,  9)

print(record[birth_year])

name = slice(0, 3)
aa = record[name]

print(aa)


code = "2011 2012 2013 2014 2015 1995 1994"

scode = slice(0, len(code))

print(code[scode])


scode = slice(0, 10)
print(code[scode])

scode = slice(0, 10, 4)
print(code[scode])


print()
print()
print()

# indices(len)
record1 = "고길동1503232340459서울"
print(len(record1))


print(name.indices(len(record1)))
