# list01 = list(range(1, 11))
# list02 = [i ** 2 for i in list01]
# print(list02)
#
# list03 = [i for i in list01 if i % 2]
# print(list03)
#
# list04 = [i + 10 for i in list01 if not i % 2]
# print(list04)
#
# list05 = [i for i in list01 if i > 5]
# print(list05)

result = []
for i in ["a", "b", "c"]:
    for j in ["A", "B", "C"]:
        result.append(i + j)
print(result)

list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
result1 = [i + j for i in list01 for j in list02]
print(result)
