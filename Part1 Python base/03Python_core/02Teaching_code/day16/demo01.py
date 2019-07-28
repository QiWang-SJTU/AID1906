"""
    迭代 --> yield
    练习:exercise02
"""


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        number = -1
        while number < self.end - 1:
            number += 1
            yield number

        # print("准备数据")
        # yield 0
        # print("准备数据")
        # yield 1
        # print("准备数据")
        # yield 2
        # print("准备数据")
        # yield 3
        # print("准备数据")
        # yield 4

        # yield 在标记,你看见的代码在执行过程中会转换为迭代器.
        # 如何生成迭代器的代码?

my = MyRange(99999999999999999999999999)
iterator = my.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 调用一次  计算一次  返回一次
# 没有将所有结果存储在内存中
# for item in MyRange(5):#[0 1 2 3 4]
#     print(item)
