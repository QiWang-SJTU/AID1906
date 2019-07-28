# 用循环来做

find_num = 0

while find_num < 3:
    str_grade = input("请输入成绩： ")
    if not str_grade:
        break

    float_grade = float(str_grade)
    if float_grade < 0 or float_grade > 100:
        print("成绩输入有误")
        find_num += 1
    elif float_grade >= 90:
        print("优秀")
    elif float_grade >= 80:
        print("良好")
    elif float_grade >= 60:
        print("及格")
    else:
        print("不及格")

else:
    print("录入成绩错误次数过多")
