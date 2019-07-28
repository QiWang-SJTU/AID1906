# 练习1:获取列表中所有整数
# 练习2:获取列表中所有大于10的小数
# 要求:分别使用列表推导式/生成器表达式/生成器函数

list01 = ["a",True,556,"7",10.3,3.7,10]
re01 = [item for item in list01 if type(item) == int ]
for item in re01:
    print(item)

re02 = (item for item in list01 if type(item) == int )
for item in re02:
    print(item)

def find_int():
    for item in list01:
        if type(item) == int:
            yield item

re = find_int()
for item in re:
    print(item)

# -------------------
for item in [item for item in list01 if type(item) == float and item >10 ]:
    print(item)

for item in (item for item in list01 if type(item) == float and item >10):
    print(item)

def find_float():
    for item in list01:
        if type(item) == float and item > 10:
            yield item

for item in find_float():
    print(item)







