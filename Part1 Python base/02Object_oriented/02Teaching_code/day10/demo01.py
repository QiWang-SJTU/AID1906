"""
    实例成员
        记住一句话:实例成员,使用对象地址访问.
    练习:exercise01.py
    练习:exercise02.py
"""


class Wife:
    pass


w01 = Wife()
# 定义实例变量: 对象.变量名 = ?
w01.name = "赵敏"
print(w01.name)

w02 = Wife()
# print(w02.name)# 错误.因为w02指向的对象,没有创建过实例变量name
print(w01.__dict__)  # 通过__dict__获取当前对象的所有实例变量
print(w02.__dict__)


class Wife2:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # 实例方法
    def print_self(self):
        print(self.name, self.height)


w01 = Wife2("灭绝", 2.3)
w02 = Wife2("金毛狮王", 3.3)
# 建议:实例方法,通过对象地址访问.
w01.print_self()
# 不建议:Wife2.print_self()# 没有传递对象地址,实例方法不能正确访问对象数据.
Wife2.print_self(w02)
