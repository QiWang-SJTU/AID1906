"""
    python高级
    1. 模块和包
        导包的路径从项目根目录开始计算.
        是否成功导入?取决于导包的路径与sys.path中的路径拼接后是否可以正确定位模块.
    2. 异常处理
        异常现象:报错后返回给调用者,不会向下执行.
        处理目的:让异常变为正常(自上而下向后执行)
    3. 迭代
        class 可迭代对象:
            def __iter__(self):
                return 迭代器()

        class 迭代器:
            def __next__(self):
                if 没有元素了:
                    raise StopIteration
                return 数据

        iterator = 可迭代对象.__iter__()
                    iter(可迭代对象)
        while True:
            try:
                item = iterator.__next__()
            except StopIteration:
                break

    能被for的条件:对象具有__iter__函数
    迭代设计思想:使用者只需通过一种方式，便可获取元素。

    4.生成器
        特点：执行一次，计算一次，返回一次

        class 生成器:
            def __iter__(self):
                return self

            def __next__(self):
                if 没有元素了:
                    raise StopIteration
                return 数据


        生成器函数：通过yield语句将函数分割为多个__next__方法.
            def 名称():
                ...
                yield 数据
                ...
        生成器表达式：列表推导式的语法

        函数式编程
            函数作为参数
            函数作为返回值
                装饰器...
"""


def fun01():
    for i in range(5):
        data = yield i
        if data == "qtx":
            yield "ｑｔｘ来啦"


iterator = fun01()  # 创建生成器对象
# __next__的返回值是yield后面的数据
print(iterator.__next__())  # 获取一个数据
print(iterator.__next__())  # 获取一个数据
# send 的参数赋值给yield前面的变量
print(iterator.send("qtx"))
print(iterator.__next__())  # 获取一个数据
print(iterator.send(""))# 获取一个数据
