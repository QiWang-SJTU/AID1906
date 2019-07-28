"""
    参照下列代码现象,自定义MyRange类,实现相同功能.
    for item in MyRange(n):
        print(item)#0 1 2 3 4 ... n-1

    for item in range(5):
        print(item)#0 1 2 3 4
"""


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)

class MyRangeIterator:
    def __init__(self, end):
        self.begin = -1
        self.end = end

    def __next__(self):
        self.begin += 1
        if self.begin == self.end:
            raise StopIteration
        return self.begin

# 调用一次  计算一次  返回一次
# 没有将所有结果存储在内存中
for item in MyRange(9999999999999999999):#[0 1 2 3 4]
    print(item)

# iterator = MyRange(5).__iter__()
#
# item = iterator.__next__()
# #0  1  2
