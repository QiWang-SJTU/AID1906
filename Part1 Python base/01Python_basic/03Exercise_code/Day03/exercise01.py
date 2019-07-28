while True:

    season = input("请输入季度： ")
    if season in ['春', '夏', '秋', '冬']:

        if season == "春":
            print(str(3) + "月" + " " +
                  str(4) + "月" + " " +
                  str(5) + "月" + ".")

        elif season == "夏":
            print(str(6) + "月" + " " +
                  str(7) + "月" + " " +
                  str(8) + "月" + ".")

        elif season == "秋":
            print(str(9) + "月" + " " +
                  str(10) + "月" + " " +
                  str(11) + "月" + ".")

        else:
            print(str(12) + "月" + " " +
                  str(1) + "月" + " " +
                  str(2) + "月" + ".")

        if input("按下q键退出：") == 'q':
            break
    else:
        print("输入错误.")
