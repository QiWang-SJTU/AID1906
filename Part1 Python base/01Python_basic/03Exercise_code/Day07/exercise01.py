# set_output = set()
# while True:
#     str_input = input("请输入字符串：")
#     if not str_input:
#         break
#     set_output.add(str_input)
#
# # print(set_output)
# for item in set_output:
#     print(item)


set_01 = {i for i in range(10)}
print(set_01)

set_02 = {i for i in range(10) if i > 5}
print(set_02)

set_03 = frozenset(range(10))
print(set_03)
print(type(set_03))
for i in set_03:
    print(i)
