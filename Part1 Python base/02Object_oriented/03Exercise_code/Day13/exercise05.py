class A:
    def m(self):
        print("A")


class B(A):
    def m(self):
        print("B")


class C(A):
    def m(self):
        print("C")


class D(B, C):
    def m(self):
        print("D")
        super().m()

d = D()
d.m()
print(D.mro())
