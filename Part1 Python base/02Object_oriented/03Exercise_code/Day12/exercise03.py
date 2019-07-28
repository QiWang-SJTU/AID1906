class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


class ElectricCar(Car):
    def __init__(self, battery, power, brand, price):
        super().__init__(brand, price)
        self.battery = battery
        self.power = power


ec1 = ElectricCar(100, 100, "BWM", 25)
print(ec1.brand)
print(ec1.price)

from exercise02 import Animal

a01 = Animal()
