# 生成器函数
def my_range(end):
    number = -1
    while number < end - 1:
        number += 1
        yield number


# for item in my_range(5):
#     print(item)

# 生成器 = 可迭代对象 + 迭代器


list01 = [5, 1, 7, 5, 4, 6, 10]


def get_num(list_target):
    list_res = []
    for item in list_target:
        if not item % 2:
            list_res.append(item)
    return list_res  # 一去不复返, 如果返回多个结果必须先整体存起来再返回


def get_res(list_target):  # 调函数不执行, 返回生成器对象 = 可迭代对象 + 迭代器
    for item in list_target:
        if not item % 2:
            yield item  # 暂时离开


print(get_num(list01))

# def get_res(list_target):
#     index = 0
#     while index < len(list_target):
#         if not list01[index] % 2:
#             yield list_target[index]
#         index += 1
#
#
# for i in get_res(list01):
#     print(i)
