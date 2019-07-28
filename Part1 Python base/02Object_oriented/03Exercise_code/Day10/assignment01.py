class Student:
    def __init__(self, name, sex, score, age):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age

    def print_self(self):
        print(self.name, self.sex, self.score, self.age)


list_student = [
    Student("无忌", "男", 86, 28),
    Student("赵敏", "女", 99, 26),
    Student("周芷若", "女", 79, 24),
    Student("灭绝", "女", 53, 80),
]


def select_info():
    dict_student = {}
    for i in range(len(list_student)):
        dict_student[list_student[i].name] = {"score": list_student[i].score,
                                              "age": list_student[i].age}
    return dict_student


dict_info = select_info()
print(dict_info["无忌"])
