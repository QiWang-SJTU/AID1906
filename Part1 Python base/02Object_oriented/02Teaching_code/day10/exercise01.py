"""
    画出内存图
"""
class Wife:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def print_self(self):
        print(self.name, self.height)


# 构造函数init:将数据传递给创建的对象.
w01 = Wife("翠花", 2.1)  # 调用了构造函数init
# 将老婆对象地址赋值给w02(两个变量指向同一个老婆对象)
w02 = w01
# 通过其中一个变量修改老婆姓名
w01.name = "翠翠"
# 通过另外一个变量访问老婆信息
w02.print_self()  # "翠翠"  2.1

list01 = [w01, w02, Wife("如花", 1.8)]
list02 = list01
list01[2].height = 1.9
list02[2].print_self()# ??


















