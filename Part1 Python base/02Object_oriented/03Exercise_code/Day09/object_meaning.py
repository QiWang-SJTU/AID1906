# class Person:
#     name = "WQ"
#
#
# class People(object):
#     name = "WYR"
#
#
# if __name__ == "__main__":
#     x = Person()
#     print("Person", dir(x))
#     y = People()
#     print("People", dir(y))

# 发现结果没有区别，python3中已经默认加载了object，即使没写
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息

