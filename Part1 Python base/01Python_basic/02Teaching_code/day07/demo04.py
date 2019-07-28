"""
    列表推导式嵌套
    练习:exercise08.py
"""
list01 = ["a","b"]
list02 = ["A","B","C"]
list_result = []

# list01[0]  +  list02[0]
# list01[0]  +  list02[1]
# list01[0]  +  list02[2]

# for c in range(3):
#     list_result.append(list01[0] + list02[c])
#
# for c in range(3):
#     list_result.append(list01[1] + list02[c])

# for r in range(2):
#     for c in range(3):
#         list_result.append(list01[r] + list02[c])

for r in list01:
    for c in list02:
        list_result.append(r + c)

list_result = [r + c for r in list01 for c in list02]
print(list_result)





