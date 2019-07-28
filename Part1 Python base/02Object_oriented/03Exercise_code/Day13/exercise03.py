"""
    运算符重载（重写）
"""


class Vector:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "%d" % self.x

    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x)
        else:
            return Vector(self.x + other)

    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.x - other.x)
        else:
            return Vector(self.x - other)

    def __mul__(self, other):
        if type(other) == Vector:
            return Vector(self.x * other.x)
        else:
            return Vector(self.x * other)


v01 = Vector(10)
v02 = Vector(5)
print("-------乘法--------")
print(v01 * v02)
