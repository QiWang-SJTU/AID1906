def fun1():
    print("hello")


def fun2():
    print("world")


# 绑定函数体,可以调用a
a = [fun1, fun2]
print(a)

# 绑定函数返回值
a = [fun1(), fun2()]

for i in a:
    i()
