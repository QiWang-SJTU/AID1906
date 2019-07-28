"""
    封装
        设计思想
"""


# 以面向对象的思想,描述下列场景:
# 老张开车去东北.
class Person:
    def __init__(self, name=""):
        self.name = name

    # 需求:人的go_to方法,调用车的run方法
    # 技术:实例方法 -- 通过对象调用
    def go_to(self, str_position, type):
        print("去:", str_position)
        type.run()


class Car:
    def run(self):
        print("走你....")


c01 = Car()
lz = Person("老张")
lz.go_to("东北", c01)
