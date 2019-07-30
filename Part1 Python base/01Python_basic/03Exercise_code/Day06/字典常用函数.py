dict_01 = {"张无忌": 24, "赵敏": 20, "张翠山": 40}

# 1. 查找
# get(key, default = None)
# 功能：返回指定键的值，如果键不在字典中返回default值
# 参数：key, default = None
# 返回值：返回指定键的值，如果键不在字典中返回default值
print(dict_01.get("张无忌"))
print(dict_01.get("张三丰"))

# setdefault(key, default = None)
# 功能：返回指定键的值，但如果键不存在于字典中，将会添加键并将值设为default
# 参数：key, default = None
# 返回值：返回指定键的值，如果键不在字典中返回default值
print(dict_01.setdefault("张无忌"))
print(dict_01.setdefault("张三丰"))
print(dict_01)

# popitem()
# 功能：随机返回并删除字典中的一对键和值(一般删除末尾对)
# 参数：None
# 返回值：元组类型的键值对
print(dict_01.popitem())

# pop()
# 功能：删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
# 参数：key: 要删除的键值 default: 如果没有 key，返回 default 值
# 返回值：返回值为被删除的值
print(dict_01.pop("张无忌"))

# items()
# 功能：以列表返回可遍历的(键, 值) 元组数组
# 参数：None
# 返回值：返回可遍历的(键, 值) 元组数组 
items = dict_01.items()
print(type(items)) # dict_items 类型
print(list(items))
for key, value in dict_01.items():
    print(key, value)

# keys()
# 功能：返回一个迭代器，可以使用 list() 来转换为列表
# 参数：None
# 返回值：返回一个迭代器
keys = dict_01.keys() # dict_keys类型
print(keys)
print(list(keys)) 

# values()
# 功能：返回一个迭代器，可以使用 list() 来转换为列表
# 参数：None
# 返回值：返回一个迭代器
values = dict_01.values() # dict_values类型
print(values)
print(list(values))

# key in dict
# 功能：判断键是否存在于字典中
# 参数：key -- 要在字典中查找的键
# 返回值：键在字典 dict 里返回 true，否则返回 false
print("赵敏" in dict_01)

# 2. 修改
# update(dic2)
# 功能：把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
# 参数：dict2 -- 添加到指定字典dict里的字典
# 返回值：None
dict1 = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female' }
 
dict1.update(dict2)
print ("更新字典 dict1 : ", dict1)

# clear()
# 功能：删除字典内所有元素
# 参数：None
# 返回值：None