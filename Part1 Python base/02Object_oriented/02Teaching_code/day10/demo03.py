"""
    封装
        数据: 老婆(名字,高度,体重)  学生(姓名,成绩,性别,年龄)
             字典(名称,单价...)
        行为: 必要
"""


class Wife:
    def __init__(self, name, age):
        self.name = name
        # 私有成员:以双下划线开头
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise ValueError("我不要")


w01 = Wife("小乔", 25)
# 不能访问私有变量
# print(w01.__age)
# w01.set_age(30)
print(w01.get_age())
