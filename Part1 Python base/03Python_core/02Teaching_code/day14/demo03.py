"""
    模块相关概念
"""

from module05 import *

fun01()
# 1. 隐藏模块成员
# _fun02()# 不能访问隐藏成员
# fun03()# 不能访问__all__以外的成员

# from module05 import _fun02
# _fun02()# 能访问隐藏成员

# from module05 import fun03
# fun03() # 能访问__all__以外的成员

# 2. 查看当前模块的文档注释
print(__doc__)

# 3. 查看当前模块的文件路径
# /home/tarena/1906/month01/code/day14/demo03.py
print(__file__)

# 4.查看当前模块名称 --- 判断当前模块是否为主模块
if __name__ == "__main__":
    print("是主模块(程序从当前模块开始执行)")

from package01.package02 import *

module03.fun01()
