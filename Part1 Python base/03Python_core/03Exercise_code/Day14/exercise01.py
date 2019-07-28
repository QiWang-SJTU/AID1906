# 一个模块只会被导入一次，不管你执行了多少次import。
# 这样可以防止导入模块被一遍又一遍地执行。

# 方法一
# 本质：使用变量module01存储该模块地址
# 优点：不用担心成员冲突问题
import module01

module01.my_fun01()

class01 = module01.Myclass01(10)
print(class01.a)
class01.fun02()

module01.Myclass01.fun03()

# 方法二
from module01 import my_fun01, Myclass01

my_fun01()
class02 = Myclass01(10)
print(class02.a)
class02.fun02()
Myclass01.fun03()

# 方法三 --->对模块内容很清楚的情况下用
from module01 import *

my_fun01()
class03 = Myclass01(10)
print(class03.a)
class03.fun02()
Myclass01.fun03()

# from module01 import A as B
#
# a = B()
# a.pri()


# from module01 import my_fun01 as f
# from module01 import Myclass01 as Class1 类的别名大写
#
# f()
# Class1.fun03()


# import module01
#
# a = module01.Myclass01(10, 20)
# a.fun02()
