tall = float(input("请输入身高： "))
weight = float(input("请输入体重： "))
bmi = weight / (tall ** 2)

if bmi > 0:
    if bmi >= 40:
        print("III度肥胖.")
    elif bmi >= 30:
        print("II度肥胖.")
    elif bmi >= 28:
        print("I度肥胖.")
    elif bmi >= 24:
        print("超重.")
    elif bmi >= 18.5:
        print("体重正常.")
    else:
        print("体重过轻")
else:
    print("计算错误")
