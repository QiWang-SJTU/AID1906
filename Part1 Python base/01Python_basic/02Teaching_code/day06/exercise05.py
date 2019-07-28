# 练习:在控制台中循环录入人的信息(姓名,年龄,性别,体重)
#          如果名称为空字符串,停止录入.
#      -- 将所有人的信息打印出来(一人一行)
# 数据结构：字典内嵌列表
# {
#   “无忌”:[28,"男",80],
#   “赵敏”:[26,"女",50],
# }

dict_person_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    weight = float(input("请输入体重："))
    dict_person_info[name] = [age, sex, weight]

for k_name, v_info in dict_person_info.items():
    # print("%s的年龄是%d,性别是%s,体重是%f")
    print("%s--%d--%s--%.1f" % (k_name, v_info[0], v_info[1], v_info[2]))
