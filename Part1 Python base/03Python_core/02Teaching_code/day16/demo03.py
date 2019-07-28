"""
    生成器表达式
    练习:exercise06
    练习:exercise07
"""

list01 = [4,5,"a",67,3.5,"b",True]

"""
def find_str():
    # result = []
    # for item in list01:
    #     if type(item) == str:
    #         result.append(item)
    # return result
    return [item for item in list01 if type(item) == str]

re = find_str()
for item in re:
    print(item)
"""
# 生成器函数
# def find_str():
#     for item in list01:
#         if type(item) == str:
#             yield item

# re = find_str()
# for item in re:
#     print(item)

# 生成器表达式
re = (item for item in list01 if type(item) == str)
for item in re:
    print(item)




