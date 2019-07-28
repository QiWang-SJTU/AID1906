"""
    zip函数
"""


# def my_zip(list_a, list_b):
#     for i in range(min(len(list_a), len(list_b))):
#         yield list_a[i], list_b[i]


def my_zip(*args):
    for i in range(len(args[0])):
        # list_temp = []
        # for item in args:
        #     list_temp.append(item[i])
        yield tuple([item[i] for item in args])


list01 = ['无忌', "赵敏", "周芷若"]
list02 = [101, 102, 103]
for item in my_zip(list01, list02):
    print(item)
