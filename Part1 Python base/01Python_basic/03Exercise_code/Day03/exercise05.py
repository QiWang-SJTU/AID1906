grade = float(input("请输入成绩： "))

if 0 <= grade <= 100:
    if grade >= 90:
        print("优秀")
    elif grade >= 80:
        print("良好")
    elif grade >= 60:
        print("及格")
    else:
        print("不及格")

else:
    print("成绩无")

