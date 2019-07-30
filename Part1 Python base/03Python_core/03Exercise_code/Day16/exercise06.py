# 可迭代对象
class MyRange:
    def __init__(self, num=0):
        self.__num = num

    def __iter__(self):
        return MyRangeIterator(self.__num)

# 迭代器
class MyRangeIterator:
    def __init__(self, end):
        self.__end = end
        self.begin = -1

    def __next__(self):
        self.begin += 1
        if self.begin == self.__end:
            raise StopIteration
        return self.begin


for i in MyRange(5):
    print(i)

# for循环三要素：
# 1. 可迭代对象 ---> __iter__()方法
# 2. 迭代器 ---> __next__()方法
# 3. 停止迭代的异常 ---> raise StopIteration