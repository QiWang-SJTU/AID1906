# 练习:自定义函数my_enumerate,实现以下功能
list01 = [4, 5, 5, 56, 6, 77]
# for item in enumerate(list01):
#     print(item)# (索引, 元素)


def my_enumerate(list_target):
    index = 0
    for item in list_target:
        yield (index,item)
        index +=1


for item in my_enumerate(list01):
    print(item)# (索引, 元素)

for index,item in my_enumerate(list01):
    print(index,item)












