"""
    函数：【一个】功能
    返回值：做函数的人，给用函数的人的结果
    练习：exercise11.py
    练习：exercise12.py
"""


# 小李同学
# 定义两个数字相加的函数
def add(number_one, number_two):
    # 逻辑处理
    return number_one + number_two  # 返回结果，退出方法
    print("看见我了吗？")  # return 以后的语句不在执行


# 获取数据
one = int(input("请输入第一个整数："))
two = int(input("请输入第二个整数："))
re = add(one, two)
# 显示结果
print("结果是：" + str(re))
