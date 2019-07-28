"""
    元组
    练习:exercise02.py
    练习:exercise03.py
"""

# 1. 创建元组
# 空元组
tuple01 = ()
tuple01 = tuple()

# 具有默认值元组
tuple02 = (1,2)

# 预留空间的存储机制 --> 按需分配的存储机制
list01 = ["a","b"]
tuple02 = tuple(list01)
print(tuple02)
# 按需分配的存储机制 --> 预留空间的存储机制
list02 = list(tuple02)
print(list02)

# tuple02 = ("a")# 不是元组
tuple02 = ("a",)# 注意:如果元组只有一个元素，必须要在末尾添加逗号
print(tuple02)

# 多个变量 = 序列
name01,name02 = ("无忌","翠山")
print(name01)
print(name02)

tuple03 = ("a","b","c","d")
# 获取元素
#   单个元素
print(tuple03[2])
#   多个元素
print(tuple03[1:3])# ("b","c")
#   所有元素
#     正向
for item in tuple03:
    print(item)
#     反向
for i in range(len(tuple03)-1,-1,-1):
    print(tuple03[i])




