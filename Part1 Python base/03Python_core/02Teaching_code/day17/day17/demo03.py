"""
    Enclosing  外部嵌套作用域
"""

# 外部
def fun01():
    # 对于fun01而言,a是局部变量
    # 对于fun02而言,a是外部嵌套变量
    a = 10
    # 内部
    def fun02():
        b = 20
        # 可以访问外部变量
        # print(a)
        # 并没有修改外部变量,而是创建了局部变量.
        # a = 100
        # 声明外部变量
        nonlocal a
        a = 100
    fun02()
    print(a)

fun01()