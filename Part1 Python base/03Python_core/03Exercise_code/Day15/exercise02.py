def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
            return score
        except:
            print("输入有误")


# get_score()

def get_age():
    while True:
        try:
            age = int(input("请输入年龄："))
            if 23 <= age <= 30:
                return age
        except:
            print("输入有误")


get_age()
