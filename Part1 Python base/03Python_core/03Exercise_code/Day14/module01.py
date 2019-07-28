def my_fun01():
    print("my_fun01")


class Myclass01:
    def __init__(self, a):
        self.a = a
        # self.__b = b

    def fun02(self):
        print("fun02")
        # print(self.__b)

    @classmethod
    def fun03(cls):
        print("fun03")
