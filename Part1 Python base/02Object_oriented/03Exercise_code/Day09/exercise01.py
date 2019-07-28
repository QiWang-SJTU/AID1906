"""
    定义类---->抽象
"""


class Wife:
    # 数据
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # 行为
    # self是位置形参，通过对象地址调用方法会自动传递对象地址。
    # 方法只有一个，在方法区。可以访问不同的对象数据。每次调用时开栈帧，调用结束后栈帧销毁
    def play(self):
        # 方法可以访问数据
        print(self.name + "在玩耍")


# 调用__init__()方法，向变量传递数据
my_wife = Wife("翠花", 1.8, 180)
my_wife.play()


class Dog:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def eat(self):
        print(self.name + "能吃")


dog1 = Dog("WW", "male")
dog1.eat()
print(dog1.sex)
print(dog1.name)

dog2 = Dog("QQ", "female")
dog2.eat()
