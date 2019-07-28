class MyRange:
    def __init__(self, num=0):
        self.__num = num

    def __iter__(self):
        number = -1
        while number < self.__num - 1:
            number += 1
            yield number


for i in MyRange(5):
    print(i)
