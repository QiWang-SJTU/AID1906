# 练习: 对象计数器
#     定义老婆类(名字),创建3个老婆对象.
#     使用类变量统计创建老婆对象的数量.
#     使用类方法,打印老婆的数量.
#     画出内存图


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("我娶了",cls.count,"个老婆")

    def __init__(self,name):
        # 实例变量: 每个都有自己的姓名
        self.name = name
        Wife.count += 1

w01 = Wife("大乔")
w01 = Wife("小乔")
w01 = Wife("西施")

Wife.print_count()



