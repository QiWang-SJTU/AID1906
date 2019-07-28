def my_enumerate(list_target):
    index = -1
    for item in list_target:
        index += 1
        yield index, item


list01 = [5, 1, 7, 5, 4, 6, 10]
for i in my_enumerate(list01):
    print(i)

for i in enumerate(list01):
    print(i)

for index, item in enumerate(list01):
    print(index, item)
