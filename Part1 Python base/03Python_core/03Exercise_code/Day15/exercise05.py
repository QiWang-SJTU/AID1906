class FigureManager:
    def __init__(self):
        self.__all_list = []

    def add_figure(self, figure_name, figure_function):
        self.__all_list.append((figure_name, figure_function))

    def __iter__(self):
        return FigureIterator(self.__all_list)


class FigureIterator:
    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        return self.__target[self.__index]


manager = FigureManager()
manager.add_figure("圆形", "a")
manager.add_figure("矩形", "b")
manager.add_figure("三角形", "c")

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item[0], item[1])
    except StopIteration:
        break
