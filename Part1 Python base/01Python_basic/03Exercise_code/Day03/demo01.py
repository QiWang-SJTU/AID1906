def gcd(a, b):
    if a == 0:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


x = int(input("Number1: "))
y = int(input("Number2: "))

print(gcd(x, y))
