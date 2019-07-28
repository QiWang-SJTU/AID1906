"""
4. 在控制台中获取一个整数，作为边长。
    打印矩形。
    例如：边长4
    ****
    *  *
    *  *
    ****
    例如：边长6
    ******
    *    *
    *    *
    *    *
    *    *
    ******
"""

number = int(input("请输入整数："))
# 上边
print("*" * number)
# 中间
for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")
# 底边
print("*" * number)
