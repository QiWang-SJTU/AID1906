"""
    封装
        行为: property
        练习:exercise05.py
"""


class Wife:
    def __init__(self, name, age):
        self.name = name
        # self.set_age(age)
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 类变量
    # property 属性: 在拦截对age的读写操作
    age = property(get_age, set_age)


w01 = Wife("小乔", 25)
# print(w01.get_age())
print(w01.age)
