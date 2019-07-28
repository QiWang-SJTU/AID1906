"""
    多继承
    17:00
"""


class A:
    def m(self):
        print("A--m")


class B(A):
    def m(self):
        print("B--m")


class C(A):
    def m(self):
        print("C--m")


class D(C, B):
    def m(self):
        # super().m()#C
        # 如果希望调用指定父类的方法,使用类名调用实例方法.
        B.m(self)
        print("D--m")

d = D()
d.m()
# python 同名方法解析顺序
print(D.mro())
