list_body = []
while True:
    name_people = input("请输入姓名： ")
    if not name_people:
        break
    age_people = int(input("请输入年龄： "))
    gen_people = input("请输入性别： ")
    weight_people = float(input("请输入体重： "))

    dict_body = {"Name": name_people,
                 "Age": age_people,
                 "Sex": gen_people,
                 "Weight": weight_people}
    list_body.append(dict_body)

for i in range(len(list_body)):
    print("%s的年龄是%d, 性别是%s, 体重是%.0f." %
          (list_body[i]["Name"],
           list_body[i]["Age"],
           list_body[i]["Sex"],
           list_body[i]["Weight"]))
