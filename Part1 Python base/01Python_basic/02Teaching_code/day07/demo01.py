"""
    集合
        不能重复  --->  将其他具有重复元素的容器转换为集合(去重复)
        数学运算  --->
    练习:exercise01.py
"""

# 创建空集合
s01 = set()
print(type(s01))


# 创建具有默认值的集合
s02 = {"a","b"}
s02 = set("abcabc")#
print(s02)
tuple02 = tuple(s02)


# 增加
s02.add("qtx")
s02.add("mly")

# 删除
s02.remove("mly")# 如果没有该元素 则报错
print(s02)

# 获取所有
for item in s02:
    print(item)

# 数学运算
# 交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2  # {2, 3}
print(s3)

# 并集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # {1, 2, 3, 4}
print(s3)

# 对称补集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2  # {1, 4}  等同于(s1-s2 | s2-s1)
print(s3)

# 补集
print(s2 - s1)# {4}
print(s1 - s2)# {1}

# 子集超集
s1 = {1, 2, 3}
s2 = {2, 3}
print(s2 < s1)  # True
print(s1 > s2)  # True


