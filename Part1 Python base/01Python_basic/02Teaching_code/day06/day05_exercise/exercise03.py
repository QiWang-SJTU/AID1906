"""
    画出内存图
"""

list01 = ["a", "b", "c"]
# 修改列表第一个元素
# 将新列表地址赋值给list01的第一个元素
list01[0] = ["A", "B"]
# 修改列表第二个元素
# 遍历新列表，将元素赋值给list01的第二个位置
list01[1:2] = ["悟空"]
print(list01)  # ?
list02 = list01[::-1]
print(list02)
print(list01[0] is list02[-1])
list01[0] = "老大"
print(list02[0])















