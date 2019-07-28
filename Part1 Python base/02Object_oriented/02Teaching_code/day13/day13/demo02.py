"""
    运算符重载(重写)
"""


# 多态:调用父,执行子.
class Vector:
    """
        向量
    """

    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "分量是:" + str(self.x)

    # 算数运算符 --> 返回新结果
    def __add__(self, other):
        """
             当前对象与其他数据相加时被自动调用
        :param other: 其他数据
        :return: 向量
        """
        # 如果other 是 向量
        if type(other) == Vector:
            return Vector(self.x + other.x)
        # 否则
        else:
            return Vector(self.x + other)

    def __rsub__(self, other):
        return Vector(other - self.x)

    # 复合运算符 --> 在原有对象基础上修改
    def __iadd__(self, other):
        self.x += other
        return self

    def __gt__(self, other):
        return self.x  > other.x

# 1. 算数运算符
v01 = Vector(10)
# 自定义向量 + 整数  -->  向量
print(v01 + 5)  # v01.__add__(5)
# 自定义向量 + 自定义向量  -->  向量
v02 = Vector(2)
print(v01 + v02)

# 2. 反向算数运算符
# 整数 - 自定义向量 --> 向量
print(5 - v01)  # v01.__rsub__(5)

"""
list01 = [1]

# print(id(list01))
list01 += [2]# 在原有基础上增加新元素
# print(id(list01))

# print(id(list01))
list01 = list01 + [3]# 产生新的对象
# print(id(list01))

print(list01)
"""

# 3. 复合运算符
#       默认使用算数运算符
print(id(v02))
v02 += 3  # v02 = v02 + 3
print(v02)
print(id(v02))

# 4. 比较运算符
# 自定义类 > 自定义类
print(v01 > v02)# v01.__gt__(v02)






