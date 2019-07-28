list01 = [1, 12.2, 3, 4, 7.2, "a"]
#
# result01 = [item for item in list01 if type(item) == int]  # 一直在执行这条语句，直到遍历完列表里的所有元素，才跳转到第二句
# for item in result01:
#     print(item)
#
# re01 = (item for item in list01 if type(item) == int)  # 生成器，每次取列表里的一个元素判断，满足条件则输出
# for item in re01:
#     print(item)
#
#
# def my_result01(list_target):
#     for item in list_target:
#         if type(item) == int:
#             yield item
#
#
# for item in my_result01(list01):
#     print(item)

for item in [item for item in list01 if type(item) == float and item > 10]:
    print(item)

for item in (item for item in list01 if type(item) == float and item > 10):
    print(item)


def my_result02(list_target):
    for item in list_target:
        if type(item) == float and item > 10:
            yield item

# 如果做一次就做生成器表达式（自己用），需要用多次的话用生成器函数（给别人用）
