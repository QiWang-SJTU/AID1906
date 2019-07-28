number1 = float(input("请输入数字1： "))
number2 = float(input("请输入数字2： "))
cal = input("请输入运算符： ")

while cal in ['+', '-', '*', '/']:
    if cal == "+":
        print(number1 + number2)

    elif cal == "-":
        print(number1 - number2)

    elif cal == "*":
        print(number1 * number2)

    else:
        print(number1 / number2)

    break

else:
    print("运算符输入错误.")
