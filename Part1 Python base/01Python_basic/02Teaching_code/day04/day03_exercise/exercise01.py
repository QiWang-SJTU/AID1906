"""
4. 在控制台中获取月份，打印季度.
"""
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份输入有误")
elif month >= 10:
    print("冬天")
elif month >= 7:
    print("秋天")
elif month >= 4:
    print("夏天")
else:
    print("春天")
