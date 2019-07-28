"""
# 练习:定义父类(车,具有数据(品牌/价格))
#     定义子类(电动车,具有数据(电池容量,充电功率))
#     分别创建父子类对象,画出内存图.
"""
class Car:
    def __init__(self,max_speed = 0, brand="", price=0,):
        self.brand = brand
        self.price = price
        self.max_speed = max_speed

class Electrocar(Car):
    def __init__(self,max_speed = 0,brand="", price=0,battery_copacity = 0,charging_power = 0):
        super().__init__(max_speed,brand,price)
        self.battery_copacity = battery_copacity
        self.charging_power = charging_power

c01 = Car(220,"奥迪",1000000)
e01 = Electrocar(100,"雅迪",2000,50000,250)
