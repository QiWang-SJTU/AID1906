"""
    参照下列代码,自定义my_zip函数,实现以下功能.
"""

list01 = ["无忌","赵敏","周芷若"]
list02 = [101,102]
# for item in zip(list01,list02):
#     print(item)

# def my_zip(target01,target02):
#     for i in range(len(target01)):
#         yield target01[i],target02[i]

def my_zip(*args):#(list01,list02)
    for i in range(len(args[0])):
        # yield args[0][i],args[1][i]
        # list_temp = []
        # for item in args:
        #     list_temp.append(item[i])
        # yield tuple(list_temp)
        yield tuple([item[i] for item in args])

# for item in my_zip(list01,list02):
#     print(item)

for item in zip(list01,list02):
     print(item)








