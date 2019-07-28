"""
    列表推导式
    练习：exercise01.py
"""
# 需求1：将lie01中所有数据+1再存储另外一个列表
list01 = [5,15,55,6,6,7]

# list02 = []
# for item in list01:
#     list02.append(item + 1)
#
# list03 = [item + 1 for item in list01]
# print(list02)
# print(list03)
# 需求2：将lie01中大于10的数据，+1再存储另外一个列表

list02 = []
for item in list01:
    if item > 10:
        list02.append(item + 1)

list03 = [item + 1 for item in list01 if item > 10]
print(list02)
print(list03)

# 10:55上课









