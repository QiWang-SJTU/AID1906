month = int(input("请输入月份： "))
if 1 <= month <= 12:
    if month in [3, 4, 5]:
        print("春季")
    elif month in [6, 7, 8]:
        print("夏季")
    elif month in [9, 10, 11]:
        print("秋季")
    else:
        print("冬季")
else:
    print("输入错误")
