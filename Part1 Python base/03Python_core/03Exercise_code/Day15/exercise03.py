class AnimalNameError(Exception):
    def __init__(self, message="", code="", error_id=0):
        self.message = message
        self.code = code
        self.id = error_id


class Animal:
    def __init__(self, name=""):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            # 抛出/发送  错误信息(异常对象)
            raise AnimalNameError("我不要", "if isinstance(value, str)", 101)
            # 需要传递的信息:消息/错误代码/错误编号....


# 接收错误信息

try:
    a1 = Animal("tiger")
    print(a1.name)
except AnimalNameError as ne:
    print(ne.id)  # 信息
    print(ne.message)  # 信息
    print(ne.code)  # 信息

"""
    自定义异常类
"""


class ATKError(Exception):
    def __init__(self, message="", code="", error_id=0, solution=""):
        # 消息/错误代码/错误编号/解决方案....
        self.message = message
        self.code = code
        self.id = error_id
        self.solution = solution


class Enemy:
    def __init__(self, atk=0):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            # 抛出/发送  错误信息(异常对象)
            raise ATKError("超过范围", "if 0 <= value <= 100", 101, "0 <= value <= 100")
            # 需要传递的信息:消息/错误代码/错误编号....


# 接收错误信息
try:
    e01 = Enemy(120)
    print(e01.atk)
except ATKError as ae:
    print(ae.id)  # 编号
    print(ae.message)  # 信息
    print(ae.code)  # 代码
    print(ae.solution)  # 解决方案
