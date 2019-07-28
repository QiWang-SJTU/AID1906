"""
    导入模块
        练习1:exercise01.py
        练习2:
            将学生管理系统,分为4个模块.
            model.py   ---> XXXModel
                数据模型
            bll.py   ---> XXXController
                业务逻辑层business  logic  layer
            usl.py ---> XXXView
                界面处理层 user show layer
            main.py ---> 调用XXXView的代码
                程序入口
        15:30
"""

# 方式1
# 语法:import 模块
# 本质:使用变量module01存储该模块地址
# 优点:不用担心成员冲突问题
# 使用:需要通过变量访问
import module01

module01.fun01()

import module01 as m

m.fun01()

# 方式2
# 本质:将模块指定成员导入到当前模块作用域中
# from 模块 import 成员
# 使用:直接使用导入的成员
# 缺点:可能造成成员冲突
from module01 import fun01
from module01 import MyClass01


def fun01():
    print("demo01--fun01")


fun01()

c01 = MyClass01()
c01.fun02()

# 方式3
# from 模块 import *
# 优点:可以一次导入多个成员,避免一个一个导入.
# 缺点: 代码可读性不高,命名冲突几率更大.
from module01 import *

# from module02 import *
# from module03 import *
fun01()

c01 = MyClass01()
c01.fun02()
