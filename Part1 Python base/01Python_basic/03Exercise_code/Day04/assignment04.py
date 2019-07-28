height = 100
distance = 0
num = 0

while height / 2 > 0.01:
    distance += height * 3 / 2
    # print(distance)
    height /= 2
    # print(height)
    num += 1

print(num, distance + height, height)
