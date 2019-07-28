dict_people = {}
while True:
    name_people = input("请输入姓名： ")
    if not name_people:
        break
    age_people = int(input("请输入年龄： "))
    gen_people = input("请输入性别： ")
    weight_people = float(input("请输入体重： "))
    dict_people[name_people] = [age_people, gen_people, weight_people]

for name, info in dict_people.items():
    print("%s的年龄是%d, 性别是%s, 体重是%.0f." % (name, info[0], info[1], info[2]))

