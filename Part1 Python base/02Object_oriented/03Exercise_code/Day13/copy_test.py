import copy

a = [1, 2]
a.append(a)
print(a, id(a), id(a[2]))
b = copy.deepcopy(a)
print(b, id(b), id(b[2]))
print(a[2][2][2][2][0])
# m = [1, 2, [3]]
# n = m[:]
# n[1] = 4
# n[2][0] = 5
# print(m)
