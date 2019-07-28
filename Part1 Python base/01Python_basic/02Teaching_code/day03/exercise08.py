# 练习:循环在控制台中根据季度打印月份，直到输入q键盘为止.

while True:
    season = input("请输入季度：")
    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    elif season == "冬":
        print("10月11月12月")

    if input("输入q退出:") == "q":
        break

