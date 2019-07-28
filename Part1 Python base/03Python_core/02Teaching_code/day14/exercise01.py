# 方式一
# import module02
# module02.my_fun01()
# c01 = module02.MyClass01(10)
# print(c01.a)
# c01.fun02()
# module02.MyClass01.fun03()
# 方式二
# from module02 import my_fun01
# from module02 import MyClass01
# my_fun01()
# c02 = MyClass01(20)
# print(c02.a)
# c02.fun02()
# MyClass01.fun03()
# 方式三
from module02 import *
my_fun01()
c02 = MyClass01(20)
print(c02.a)
c02.fun02()
MyClass01.fun03()











