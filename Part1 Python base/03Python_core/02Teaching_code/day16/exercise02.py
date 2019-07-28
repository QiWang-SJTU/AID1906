"""
    改造day15/exercise07
    将图形管理器由迭代器改为yield实现.
    体会:调用一次next,计算一次,返回一次.
"""

class GraphicManager:
    def __init__(self):
        self.__all_graphic = []

    def add_graphic(self, str_graphic):
        self.__all_graphic.append(str_graphic)

    def __iter__(self):
        # return GraphicIterator(self.__all_graphic)
        # index = 0
        # while index < len(self.__all_graphic):
        #     yield self.__all_graphic[index]
        #     index +=1

        for item in self.__all_graphic:
            yield item

# class GraphicIterator:
#     def __init__(self, data):
#         self.__target = data
#         self.__index = -1
#
#     def __next__(self):
#         self.__index += 1
#         try:
#             return self.__target[self.__index]
#         except IndexError:
#             raise StopIteration

manager = GraphicManager()
manager.add_graphic("圆形")
manager.add_graphic("矩形")
manager.add_graphic("三角形")

for item in manager:
    print(item)















