"""
    继承 -- 设计(2)
    练习:exercise02
"""


# 老张开车去东北.
# 需求变化:还可能坐飞机,坐火车......

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, str_position, vehicle):
        print("去:", str_position)
        vehicle.transport()


class Vehicle:
    """
        抽象的
        交通工具
    """

    def transport(self):
        pass


# -------------------------------------
class Car(Vehicle):

    def transport(self):
        print("走你...")


class Airplane(Vehicle):

    def transport(self):
        print("嗖嗖嗖.")


c01 = Car()
a01 = Airplane()
lz = Person("老张")
lz.go_to("东北", a01)
