"""
    yield --> 生成器
    练习:exercise03
    练习:exercise04
    练习:exercise05
"""
"""
class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        number = -1
        while number < self.end - 1:
            number += 1
            yield number

my = MyRange(5)
iterator = my.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""


def my_range(end):
    number = -1
    while number < end - 1:
        number += 1
        yield number

# 调用一次 计算一次  返回一次
# 没有存储所有结果
for item in my_range(99999999999999999999999):
    print(item)













# my = my_range(5)
# iterator = my.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


