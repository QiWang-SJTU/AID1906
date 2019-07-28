# 练习1:list --> 字典,key 是列表元素，值是键的长度.
# ["无忌","翠山","张三丰"] --> {"无忌":2,"翠山":2,"张三丰":3}
list_names = ["无忌", "翠山", "张三丰"]

# dict_names = {}
# for item in list_names:
#     dict_names[item] = len(item)

dict_names = {item: len(item) for item in list_names}
print(dict_names)
