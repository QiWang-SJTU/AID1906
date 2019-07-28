# 定义:图形管理器
#        1. 记录所有图形
#        2. 提供计算总面积的方法
# 需求变化:
#        圆形(pi * r ** 2)
#        矩形(长 * 宽)
#        ...
# 测试:
# 创建图形管理器,添加圆形,矩形.
# 调用计算总面积方法.

class GraphicManager:
    """
        图形管理器
    """

    def __init__(self):
        # 存储的是具体图形
        # 所以图形管理器与图形是组合关系.
        self.__list_graphic = []

    @property
    def list_graphic(self):
        return self.__list_graphic

    def add_graphic(self, graphic):
        self.__list_graphic.append(graphic)

    def get_total_area(self):
        total_area = 0
        for item in self.__list_graphic:
            # 调用父类,执行子类.
            total_area += item.calculate_area()
        return total_area


class Graphic:
    """
        图形,抽象所有具体的图形,统一图形的计算面积方法,隔离具体图形的变化.
    """

    def calculate_area(self):
        """
            计算面积
        :return: 小数类型的面积.
        """
        pass


# ------------------------------------------

class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2

class Rectanle(Graphic):
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# ------------
manager = GraphicManager()
c01 = Circle(5)
manager.add_graphic(c01)
manager.add_graphic(Rectanle(2, 5))
print(manager.get_total_area())
