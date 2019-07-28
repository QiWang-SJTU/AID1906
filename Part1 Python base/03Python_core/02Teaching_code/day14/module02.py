"""
    练习:创建模块module02.py
        定义如下代码
        创建模块exercise01.py,
        使用三种方式导入模块
        调用函数my_fun01,实例变量a,实例方法fun02,类方法fun03
"""
def my_fun01():
    print("my_fun01")

class MyClass01:
    def __init__(self,a):
        self.a = a

    def fun02(self):
        print("fun02")

    @classmethod
    def fun03(cls):
        print("fun03")