class Animal:
    def eat(self):
        print("能吃")


class Dog(Animal):
    def run(self):
        print("能跑")


class Bird(Animal):
    def fly(self):
        print("能飞")


animal01 = Animal()
dog01 = Dog()
bird01 = Bird()

dog01.eat()
bird01.eat()

print(isinstance(animal01, Animal))
print(isinstance(animal01, Dog))
print(isinstance(animal01, Bird))

print(issubclass(Animal, Animal))
print(issubclass(Dog, Animal))
print(issubclass(Bird, Dog))

print(type(Dog) == Animal)
