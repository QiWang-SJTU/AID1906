class MyRange:
    def __init__(self, num=0):
        self.__num = num

    # 生成器函数，返回生成器对象 = 可迭代对象 + 迭代器
    def __iter__(self):
        number = -1
        while number < self.__num - 1:
            number += 1
            yield number


for i in MyRange(5):
    print(i)

# 用for循环原理解释生成器函数
my = MyRange(5)
# 调用生成器函数，不执行函数体。返回可迭代对象 + 迭代器，所以有next()方法
# 将yield以前的代码放在next()方法中
iterator = my.__iter__()
while True:
    try:
        # 调用next()方法，此时才执行生成器函数的函数体
        # 返回yield后面的数据，程序在yield处中断，下次调用时从中断处继续执行
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break