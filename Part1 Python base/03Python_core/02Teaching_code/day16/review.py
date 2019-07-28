"""
    复习
    异常处理
        异常:程序不在继续向后执行,而是返回给调用者.
        处理:让异常状态改变正常流程(向后执行)
    迭代:重复(每次参照上次结果)
        可迭代对象
            标志:__iter__(),返回值是迭代器.
            作用:可以参与for
        迭代器
            标志:__next__(),返回值是聚合对象的元素
            作用:可以迭代(挨个取元素)

        语法:
        class 可迭代对象:
            def __iter__(self):
                return 迭代器(数据)

        class 迭代器:
            def __init__(self,参数):
                self.聚合对象 = 参数
            def __next__(self):
                if 没有元素了:
                    raise StopIteration
                return 元素

        for item in 可迭代对象():
            pass

        iterator = 可迭代对象().__iter__()
        while True:
            try:
                item = iterator.__next__()
            except StopIteration:
                break


"""