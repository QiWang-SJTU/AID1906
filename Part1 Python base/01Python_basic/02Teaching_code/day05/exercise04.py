# 练习1:将列表[4,54,5,6,67,17,8]中大于10的数字存入另外一个列表中.
list01 = [4,54,5,6,67,17,8]
list_result = []
for item in list01:
    if item > 10:
        list_result.append(item)
print(list_result)

