"""
    自定义异常类
    15:20 上课
"""

class AgeError(Exception):
    def __init__(self, message="", code="", id=0):
        # 消息/错误代码/错误编号....
        self.message = message
        self.code = code
        self.id = id


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 抛出/发送  错误信息(异常对象)
            raise AgeError("我不要", "if 20 <=value <= 30", 101)
            # 需要传递的信息:消息/错误代码/错误编号....


# 接收错误信息
try:
    w01 = Wife(25)
    print(w01.age)
except AgeError as e:
    print(e.id)  # 信息
    print(e.message)  # 信息
    print(e.code)  # 信息
