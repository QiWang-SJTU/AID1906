student_name_final = []
while True:
    student_name = input("请输入所有学生姓名： ")
    if not student_name:
        print("录入结束.")
        break
    student_name_final.append(student_name)

for i in student_name_final:
    print(i)


# append()返回的是None
# a = [1, 3]
# print(a.append(1))
