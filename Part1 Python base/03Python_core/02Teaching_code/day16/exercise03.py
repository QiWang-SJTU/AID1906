# 练习1:从列表中[4,5,5,56,6,77]获取所有偶数
#      -- 定义函数,将结果存入列表,再返回列表
#      -- 定义函数,使用yield返回结果.

list01 = [4, 5, 5, 56, 6, 77]


# def get_event01():
#     先存储所有结果
#     list_result = []
#     for item in list01:
#         if item % 2 == 0:
#             list_result.append(item)
#     return list_result

# re01 = get_event01()# 调函数,立即执行函数,计算/存储所有结果.
# for item in re01:
#     print(item)

# 当函数返回多个结果时,使用yield
def get_event02():
    for item in list01:
        if item % 2 == 0:
            yield item

re01 = get_event02()# 调函数,不执行.返回生成器对象(可迭代对象+迭代器)
for item in re01:#循环时,因为内部调用了next,所以执行函数体.
    print(item)








