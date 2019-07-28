"""
    封装
        行为: 标准属性
        练习:exercise06.py
        练习:exercise07.py
"""


# 读写属性age
class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # 拦截读取 age = property(读取方法,None)
    def age(self):
        return self.__age

    @age.setter  # 拦截写入 age.setter(写入方法)
    def age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise ValueError("我不要")


w01 = Wife("小乔", 25)
# print(w01.get_age())
print(w01.age)


# ---------------------------
# 只读属性age
class Wife2:
    def __init__(self, name):
        self.name = name
        self.__age = 23

    @property  # 拦截读取 age = property(读取方法,None)
    def age(self):
        return self.__age


w02 = Wife2("大桥")


# w02.age = 30
# ---------------------
# 只写属性age
class Wife3:
    def __init__(self, name):
        self.name = name
        self.age = 23

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise ValueError("我不要")

    age = property(None, set_age)


w03 = Wife3("大桥")
w03.age = 30
# print(w03.age)# 不能读取
