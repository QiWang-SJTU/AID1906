class FigureManager:
    def __init__(self):
        self.__all_list = []

    def add_figure(self, figure_name, figure_function):
        self.__all_list.append((figure_name, figure_function))

    def __iter__(self):
        # return FigureIterator(self.__all_list)
        index = 0
        while index < len(self.__all_list):
            yield self.__all_list[index]
            index += 1


manager = FigureManager()
manager.add_figure("圆形", "a")
manager.add_figure("矩形", "b")
manager.add_figure("三角形", "c")

# for item in manager:
#     print(item)

iterator = manager.__iter__()  # 1. 调用生成器函数__iter__, 创建迭代器对象
while True:
    try:
        # 2. 调用迭代器对象的__next__方法, 此时执行生成器函数
        # 3. 每次执行到yield语句时返回数据，暂时离开
        # 4. 下次调用__next__方法时继续从离开处继续执行
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
