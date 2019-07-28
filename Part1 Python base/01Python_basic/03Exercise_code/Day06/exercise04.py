dict01 = {"张三": 19, "李四": 20}
print(dict01)

list01 = [("a", "b"), ("c", "d")]
dict02 = dict(list01)
print(dict02)

# 没有该键算添加
dict02["键"] = "值"
print(dict02)

# 有该键算修改
dict02["键"] = "值2"
print(dict02)

del dict02["键"]
print(dict02)

# 查找一定要先判断， 不然不存在会报错
if "键" in dict02:
    print(dict02["键"])
else:
    print("不存在")

# 遍历字典
for key, value in dict02.items():
    print(key, value)

# 获取所有值
for value in dict02.values():
    print(value)

# 获取所有键
for key in dict02.keys():
    print(key)

# 返回key值
for key in dict02:
    print(key)


