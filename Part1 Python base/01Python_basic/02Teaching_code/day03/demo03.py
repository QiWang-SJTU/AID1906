"""
    if的真值表达式

        if 变量:
            变量存在数据则执行

    条件表达式：
        有选择性的为变量进行赋值

    练习:exercise07.py
"""

number = 10
if number != 0:
    print("不是零")
# 1. if的真值表达式
if number:
    # if bool(number):
    print("不是零")

# 2. 条件表达式：
if input("请输入性别：") == "男":
    sex_id = 1
else:
    sex_id = 0
sex_id = 1 if input("请输入性别：") == "男" else 0
print(sex_id)


