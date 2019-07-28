
import math

# 1.封装
# 要解决图形管理器问题，需要使用多个类(单一原则)
# 包括管理器类、图形类

# 2.继承
# 针对不同的图形有不同的面积计算方法
# 为方便复用，创建一个图形父类，不同图形的类继承图形父类的方法(开闭原则、依赖倒置)

# 3.多态
# 继承同一个图形父类的方法，不同图形子类进行了方法重写，实现不同的计算功能

# 4.组合复用
# 图形管理器的计算总面积的方法通过实例变量图形列表来访问图形（圆形、矩形）的计算面积的方法


class FigureManager:
    def __init__(self):
        # 存储的是具体图形，所以图形管理器与图形是组合关系
        self.__list_graphic = []

    def add_graphic(self, graphic):
        self.__list_graphic.append(graphic)

    def cal_total_area(self):
        total_area = 0
        for item in self.__list_graphic:
            # 调用父类的一个方法，执行子类重写的方法
            total_area += item.cal_area()
        return total_area


class Figure:
    def cal_area(self):
        pass


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def cal_area(self):
        return math.pi * self.r ** 2


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def cal_area(self):
        return self.a * self.b


f01 = FigureManager()
c01 = Circle(2)
r01 = Rectangle(3, 4)
f01.add_graphic(c01)
f01.add_graphic(r01)

print(f01.cal_total_area())



