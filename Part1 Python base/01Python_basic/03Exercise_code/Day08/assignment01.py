def fun01(p1, p2, p3, p4):
    p1 = 500
    p2[0] = 600
    p3[0] = [700]
    p4[:] = [800]


a = "五百"
b = ["六百"]
c = ["七百"]
d = ["八百"]
fun01(a, b, c, d)

print(a)
print(b)
print(c)
print(d)
