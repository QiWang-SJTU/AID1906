"""
    练习:图形管理器记录多个图形(字符串)
        实现迭代图形管理器,获取所有图形的功能.
"""

class GraphicManager:
    def __init__(self):
        self.__all_graphic = []

    def add_graphic(self, str_graphic):
        self.__all_graphic.append(str_graphic)

    def __iter__(self):
        return GraphicIterator(self.__all_graphic)

class GraphicIterator:
    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        try:
            return self.__target[self.__index]
        except IndexError:
            raise StopIteration

manager = GraphicManager()
manager.add_graphic("圆形")
manager.add_graphic("矩形")
manager.add_graphic("三角形")

for item in manager:
    print(item)















