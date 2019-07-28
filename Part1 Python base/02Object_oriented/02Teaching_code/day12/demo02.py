"""
    继承 -- 数据

"""


class Person:
    def __init__(self, name=""):
        self.name = name


class Student(Person):
    def __init__(self, name="", score=0):
        self.score = score
        # self.name = name
        # 如果子类没有构造函数,使用父类构造函数
        # 如果子类有构造函数,必须铜通过super()调用父类构造函数,
        # 否则会覆盖父类(不执行)的.
        super().__init__(name)


# 创建实例变量
s01 = Student("无忌", 100)
print(s01.name)
print(s01.score)
p01 = Person("翠山")
print(p01.name)
