class Student:
    def __init__(self, name, sex, score, age):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age

    def print_self(self):
        print(self.name, self.sex, self.score, self.age)

list01 = [
    Student("无忌","男",86,28),
    Student("敏敏","女",99,26),
    Student("周芷若","女",39,24),
    Student("灭绝","女",23,80),
]

# 练习1:定义在list01中查找"赵敏"同学的函数
def find01():
    for item in list01:
        if item.name == "赵敏":
            return item

stu01 = find01()
# 如果函数没有找到,则错误.所以如果不能确定是否找到,需要判断.
# if stu01 != None:
if stu01:
    print(stu01.name)
# None.name
# AttributeError: 'NoneType' object has no attribute 'name'

# 练习2:定义在list01中查找所有女同学的函数
# 11:06
def find02():
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result

list_result = find02()# []
for item in list_result:
    item.print_self()

# 练习3:定义在list01中查找所有同学姓名的函数
# 11:18
def find03():
    result = []
    for item in list01:
        result.append(item.name)
    return result

for item in find03():
    print(item)

# 练习4:定义将list01中所有女同学的成绩+10分的函数
# 11:26
def update01():
    for item in list01:
        if item.sex == "女":
            item.score += 10

update01()
for item in list01:
    item.print_self()

# 练习5:定义函数,删除list01中所有不及格的学生
def delete01():
    for i in range(len(list01)-1,-1,-1):
        if list01[i].score <60:
            del list01[i]

print("删除...")
delete01()
for item in list01:
    item.print_self()

















