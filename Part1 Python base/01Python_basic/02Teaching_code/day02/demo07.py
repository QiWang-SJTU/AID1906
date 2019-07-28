"""
    身份运算符
"""
a = 500
b = a
c = 1000
print(id(a))  # 返回变量所指向的数据的内存地址
print(id(b))
print(id(c))
print(a is b)  # 内部：判断的就是id函数的结果
print(a is c)
