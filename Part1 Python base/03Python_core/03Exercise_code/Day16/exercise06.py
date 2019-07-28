class MyRange:
    def __init__(self, num=0):
        self.__num = num

    def __iter__(self):
        return MyRangeIterator(self.__num)


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
