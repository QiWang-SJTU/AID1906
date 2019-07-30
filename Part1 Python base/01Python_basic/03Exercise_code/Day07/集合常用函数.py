set_01 = {"张无忌", "赵敏", "张三丰"}

# update()
# 功能：修改当前集合，可以添加新的元素或集合到当前集合中
# 如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
# 参数：可以是元素或者集合
# 返回值：None
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.update(y)

print(x)

# add()
# 功能：给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
# 参数：元素
# 返回值：None
x.add("wang")
print(x)

y.add("apple")
print(y)

# clear()
# 移除集合所有元素

# copy()
# 功能：拷贝一个集合
# 参数：None
# 返回值：None
z = x.copy()
print(z)

# pop()
# 功能：对于是字典和字符转换的集合是随机删除元素的。
# 当集合是由列表和元组组成时是从左边删除元素的。
# 参数：None
# 返回值：返回移除的元素
a = x.pop()
print(a)

# 集合对list和tuple有排序功能(升序)
set_02 = set([9, 4, 5, 2, 6, 7, 1, 8])
print(set_02)  # {1, 2, 4, 5, 6, 7, 8, 9}

# discard()/remove()
# 功能：删除集合中的指定元素
# 参数：元素
# 返回值：None
# 区别：删除不存在元素时remove会报错但是discard不会
x.discard("cherry")
x.remove("banana")
print(x)
