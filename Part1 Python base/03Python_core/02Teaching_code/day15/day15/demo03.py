"""

"""

class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 20 <=value <= 30:
            self.__age = value
        else:
            # 抛出/发送  错误信息(异常对象)
            raise ValueError("我不要")


# 接收错误信息
try:
    w01 = Wife(85)
    print(w01.age)
except ValueError as e:
    print(e.args)# 信息










