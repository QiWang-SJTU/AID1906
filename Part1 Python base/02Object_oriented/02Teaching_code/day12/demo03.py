"""
    继承 -- 设计(1)
"""


# 老张开车去东北.
# 需求变化:还可能坐飞机,坐火车......

# 违背了面向对象设计原则:
#   开闭原则 /  依赖倒置
class Person:
    def __init__(self, name=""):
        self.name = name

    # 对方法增加语句,删除语句,修改语句都视为改变代码.
    def go_to(self, str_position, vehicle):
        print("去:", str_position)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.flay()


class Car:
    def run(self):
        print("走你....")


class Airplane:
    def flay(self):
        print("嗖嗖...")


c01 = Car()
a01 = Airplane()
lz = Person("老张")
lz.go_to("东北", c01)
