# 练习:在控制台中依次录入4个数字，打印最大的数。
# 算法：8   5   9   3    -->  9
# (1)假设第一个就是最大的，把它记在心里.
# (2)用心中的数字与第二个变量进行比较,如果第二个更大,则替换心中那个数。
# (3)用心中的数字与第三个变量进行比较,如果第三个更大,则替换心中那个数。
# (4)用心中的数字与第四个变量进行比较,如果第四个更大,则替换心中那个数。
number01 = float(input("请输入第一个变量："))
number02 = float(input("请输入第二个变量："))
number03 = float(input("请输入第三个变量："))
number04 = float(input("请输入第四个变量："))

max_value = number01

if max_value < number02:
    max_value = number02
if max_value < number03:
    max_value = number03
if max_value < number04:
    max_value = number04

print(max_value)

