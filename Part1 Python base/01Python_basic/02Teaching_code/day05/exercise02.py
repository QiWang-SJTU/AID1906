# 练习:在控制台中获取所有学生的姓名(循环，一个一个录入)
#     如果录入空字符串，则停止.
#     打印所有学生姓名(一行一个)

list_names = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    list_names.append(name)

for item in list_names:
    print(item)

