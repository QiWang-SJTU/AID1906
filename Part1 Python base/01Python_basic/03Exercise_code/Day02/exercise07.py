# year = int(input("请输入年份："))
# print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

a = 500
b = a
c = 1000
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)


