"""
    list --> str
    练习:exercise07.py
"""

list01 = ["a","b","c"]
str01 = "+".join(list01)# a+b+c
print(str01)


# 案例:根据某些逻辑，拼接字符串.
# str_result = ""
# for item in range(10):#0 1 2 3 4 5 6 7 8 9
#     # str_result += str(item)
#
#     # ""  +  "0"  --> 产生一个新字符串对象 "0"
#     # "0"  + "1"  --> 产生一个新字符串对象 "01"
#     # "01"  + "2"  --> 产生一个新字符串对象 "012"
#     # ...
#     str_result = str_result + str(item)
#
# print(str_result)

# 核心思想：通过可变对象(list)收集需要拼接的字符串,最后再转换为字符串。
list_result = []
for item in range(10):#0 1 2 3 4 5 6 7 8 9
    list_result.append(str(item))
str_result = "".join(list_result)
print(str_result)


