"""
    使用可迭代对象,迭代器
"""
list01 = [43,45,54,5,67]
# for item in list01:
#     print(item)

# 原理:
# 1. 调用iter方法获取迭代器对象
iterator = list01.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()# Stop Iteration
        print(item)
        # 3. 遇到"停止迭代"异常,则停止循环.
    except StopIteration:
        break

# 面试题:
# 能够参与for循环的对象,必须具备什么条件?
# 答:该对象必须具有__iter__()方法











