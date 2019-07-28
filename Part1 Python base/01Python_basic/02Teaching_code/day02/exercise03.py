"""
    练习:
    在控制台中获取一个变量
    再在控制台中获取一个变量
    交换这两个变量
    最后输出这两个变量

    提示:
    变量名称=input("提示的信息:")
    print(变量名)
"""
data01 = input("请输入第一个变量：")
data02 = input("请输入第二个变量：")

# temp = data01
# data01 = data02
# data02 = temp

data01, data02 = data02, data01

print(data01)
print(data02)
