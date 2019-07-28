"""
    内存图
    练习：exercise04.py
         exercise05.py
         exercise06.py
"""

list01 = ["无忌","翠山","三丰"]
# 将list01中存储的列表地址，赋值给list02.
list02 = list01
# 修改列表第一个元素
# list01[0] = "张无忌"
# 修改变量list01的引用(指向)
list01 = "张无忌"
print(list02[0])


# ----------------练习------------------------
# 15:15上课
list01 = [800,900,1000]
list02 = list01
list03 = list01
list01[0] = "八百"
print(list02[0])# "八百"
list03 = "九百"
print(list02)# ["八百",900,1000]

list01 = [800,900,1000]
# 通过切片创建新列表，赋值给变量list02
list02 = list01[:]
list01[0] = "八百"
print(list02[0])#?

list01 = [800,900,1000]
list02 = list01
# 定位第二个元素，然后进行修改.
list01[1:2] = ["a","b"]
print(list02)# [800, 'a', 'b', 1000]


list01 = [100,[200,300]]
list02 = list01
list01[1][0] = 500
print(list02[1][0])# 500

#------------------------

list01 = [100,[200,300]]
# list02 = list01[:]# 浅拷贝
list02 = list01.copy()# 浅拷贝
list01[1][0] = 500
print(list02[1][0])# 500


list01 = [100,200]
list02 = [100,200]
print(list01 == list02)#true 比较的是内容
print(list01 is list02)#false 比较的是地址 id(list01)  == id(list02)


# 准备拷贝工具
import copy

list01 = [100,[200,300]]
# 深拷贝(“划清界限”：拷贝前与拷贝后的对象互不影响)
# 注意：深拷贝可能占用内存过大.
list02 = copy.deepcopy(list01)
list01[1][0] = 500
print(list02[1][0])# 200












