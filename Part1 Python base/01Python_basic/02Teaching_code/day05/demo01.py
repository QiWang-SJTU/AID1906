"""
    列表：
        适用性:存储多个数据.
    练习:exercise01.py
        exercise02.py
        exercise03.py
"""

# 1. 创建列表
# 空列表
list01 = []
list01 = list()

# 具有默认值的列表
list02 = [1,"a",True]
# list02 = list(可迭代对象)
# str --> 列表
list02 = list("齐天大圣")
# range --> 列表
list02 = list(range(5))

# 2. 增加
# 追加
list02.append("qtx")
# 插入(索引,元素)
list02.insert(3,"lzmly")

# 3. 删除
# 根据元素删除
list02.remove(4)
# 根据索引删除
del list02[3]

# 4. 修改
list02[0] = "第一个元素"
print(list02)

# 5. 切片:定位多个元素
# 获取 (重新创建新列表)
# 前三个元素
list03 = list02[:3]
# 修改
# 修改后两个元素
list02[-2:] = ["倒数第2个元素","倒数第1个元素"]
print(list02)
# 通过切片定位2个元素，修改为3个元素
list02[2:4] = ["a","b","c"]
# 通过切片定位3个元素，修改为0个元素  [删除]
list02[2:5] = []
print(list02)

# 6. 查询
# 获取所有元素
for item in list02:
    print(item)

# 倒序获取所有
# 不建议通过切片(因为重新创建新列表,索引不建议.)
# for item in list02[::-1]:
#     print(item)

# 建议通过索引
#2  1  0
# for i in range(2,-1,-1):
for i in range(len(list02)-1, -1, -1):
    print(list02[i])















