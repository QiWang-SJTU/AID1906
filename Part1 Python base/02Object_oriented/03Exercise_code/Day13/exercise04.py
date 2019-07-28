"""
    反向运算符重载（重写）
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

    def __radd__(self, other):
        if type(other) == Vector:
            return Vector(other.x + self.x)
        else:
            return Vector(other + self.x)

    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.x - other.x)
        else:
            return Vector(self.x - other)

    def __rsub__(self, other):
        if type(other) == Vector:
            return Vector(other.x - self.x)
        else:
            return Vector(other - self.x)

    def __mul__(self, other):
        if type(other) == Vector:
            return Vector(self.x * other.x)
        else:
            return Vector(self.x * other)

    def __rmul__(self, other):
        if type(other) == Vector:
            return Vector(other.x * self.x)
        else:
            return Vector(other * self.x)

    def __truediv__(self, other):
        if type(other) == Vector:
            return Vector(other.x / self.x)
        else:
            return Vector(other / self.x)

    def __rtruediv__(self, other):
        if type(other) == Vector:
            return Vector(self.x / other.x)
        else:
            return Vector(self.x / other)

    def __pow__(self, power, modulo=None):
        if type(power) == Vector:
            return Vector(self.x ** power.x)
        else:
            return Vector(self.x ** power)

    def __iadd__(self, other):
        self.x += other
        return self

    def __isub__(self, other):
        self.x -= other
        return self

    def __imul__(self, other):
        self.x *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        return self


v01 = Vector(10)
v02 = Vector(5)

# 复合运算符如果不用，默认使用算数运算符
v01 /= 2
print(v01)
