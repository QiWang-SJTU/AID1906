list_01 = [(1,), (1, 2), "1", 2, 3, 4, 5, 6, 4, 6, 1]

# 1. 查找
# list.index()
# 功能：返回对应元素索引下标
# 参数：元素值及索引范围
# 返回值：对应元素索引下标
# 元素可以是任何类型，数字/字符串/元组/列表/字典等
index = list_01.index(2)
print(index)
print(list_01.index((1,)))

# 在一定范围内找，不存在时触发ValueError
index1 = list_01.index(3, 0, 5)
print(index1)

# list.count()
# 功能：统计某个元素在列表中出现的次数
# 参数：元素值
# 返回值：次数
count = list_01.count(4)
print(count)
print(list_01.count((1, 2)))
print(list_01.count(1))

a = (1)
print(type(a)) # 这样写a是整型，等同于a = 1
b = (1, ) # b是元组

# list.pop()
# 功能：删除索引对应的元素，默认删除最后一个元素
# 参数：索引值
# 返回值：删除的元素
elem = list_01.pop()
print(elem)
print(list_01.pop(0))

# 2. 修改
# list.insert()
# 功能：将某个元素插放到列表中指定的位置
# 参数：索引值，元素值
# 返回值：None
c = list_01.insert(1, 2)
print(c)

# list.remove()
# 功能：从列表中删除第一次出现在列表中的值
# 参数：元素值
# 返回值：None
d = list_01.remove(2)
print(d)
print(list_01)

# list.extend()
# 功能：向列表追加另一个列表
# 参数：列表
# 返回值：None
e = list_01.extend([2, 5, 7])
print(e)
print(list_01)

# list.reverse()
# 功能：列表的反转，用来改变原列表的先后顺序
# 参数：None
# 返回值：None
list_01.reverse()
print(list_01)

list_01.pop()
list_01.pop()
print(list_01)

# list.sort()
# 功能：将列表中的元素进行排序，默认顺序按值的小到大的顺序排列
# 参数：默认为key = None, reverse = False
# 返回值：None
list_01.sort()
print(list_01)

# key用于指定比较函数，将函数名赋值给key
# 比如说想对以下列表按照每个元组中第二个元素的大小进行排列
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
 
# 指定第二个元素排序
random.sort(key=takeSecond)
 
# 输出类别
print ('排序列表：', random)

# list.clear()
# 功能：清空列表
# 参数：None
# 返回值：None
random.clear()
print(random)

# 3. 拷贝
# list.copy()
# 功能：浅拷贝此列表（只复制一层，不会复制深层对象) 
# 参数：None
# 返回值：返回复制后的新列表
list_02 = list_01.copy()
print(list_02)