"""
    循环语句
        while 条件:
            循环体
"""

# 死循环：循环条件永远满足
while True:
    str_usd = input("请输入美元：")
    int_usd = int(str_usd)
    rmb = int_usd * 6.86
    print("人民币是："+ str(rmb))

    if input("按下q键退出:") == "q":
        break # 退出循环


