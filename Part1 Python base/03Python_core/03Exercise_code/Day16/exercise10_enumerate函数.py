def my_enumerate(list_target):
    index = -1
    for item in list_target:
        index += 1
        yield index, item


list01 = [5, 1, 7, 5, 4, 6, 10]
for i in my_enumerate(list01):
    print(i)

# 这个函数就是为了得到元素值得同时也能得到元素得索引
# 得到元组(index, elem)
for i in enumerate(list01):
    print(i)

# 直接得到索引和元素的值
for index, item in enumerate(list01):
    print(index, item)
