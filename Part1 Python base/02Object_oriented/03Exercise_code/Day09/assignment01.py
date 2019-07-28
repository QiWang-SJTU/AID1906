class Cat:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def play(self):
        print("有一只名为%s，%d岁的%s猫在玩耍" % (self.name, self.age, self.sex))


my_cat = Cat("Eva", 2, "母")
my_cat.play()


class Computer:
    def __init__(self, brand):
        self.brand = brand

    def cal(self):
        print(self.brand + "能计算")


my_computer = Computer("Lenovo")
my_computer.cal()
