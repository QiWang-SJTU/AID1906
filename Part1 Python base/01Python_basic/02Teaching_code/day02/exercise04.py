"""
练习:画出下列代码内存图
dog01 = "咪咻"
dog02 = "赵金多"
dog01 = dog02
dog03 = dog02
del dog02,dog03
"""
dog01 = "咪咻"
dog02 = "赵金多"
dog01 = dog02
dog03 = dog02
del dog02,dog03
# "金多"　还在(因为变量dog01引用着)
print(dog01)
# 访问已经删除的变量，会引发错误.
# print(dog02)
