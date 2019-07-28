

#练习1:使用for循环原理(迭代原理)打印元组中所有元素.
tuple01 = (4,55,5,46)
iterator = tuple01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key)
    except StopIteration:
        break

#练习2:不使用for循环,打印字典中所有数据(key,value)
dict01 = {"张无忌":101,"赵敏":101,"张翠山":102}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break



