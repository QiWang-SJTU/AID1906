# sum_value = 0
# for i in range(1, 51):
#     if i % 6:
#         continue
#     else:
#         print(i)
#         sum_value += i
# print(sum_value)


sum_value = 0
for i in range(10, 81):
    if (i % 10) in [2, 5, 6]:
        continue
    else:
        print(i)
        sum_value += i
print(sum_value)
