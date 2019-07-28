"""
    bool
    比较运算符
    逻辑运算符
    练习:exercise10.py
"""

# 1.    bool　          int         类型
#   True False      10  20  30 ..   数据
#   命题：带有判断性质的陈述句.
#        我是个男人  对的/真的(True)
#        我是个坏人  错的/假的(False)
#        1 > 2     错的/假的(False)

# 2. 比较运算符  >  <   >=   <=   ==  !=  结果是bool类型
#  结果 = 变量1  >  变量2
print(1 > 2)  # False

# 3. 逻辑运算符  与and　　或or　　非not
#    判断两个命题(bool值)关系
# 总结：一假俱假　　表达的是"并且”的关系(必须都满足)
print(True and True)# True
print(False and True)# False
print(True and False)# False
print(False and False)# False

# 总结：一真俱真　表达的是"或者”的关系(满足一个就行)
print(True  or True)# True
print(False or True)# True
print(True  or False)# True
print(False or False)# False
# 非
print(not True)







