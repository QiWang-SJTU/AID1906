# return本身就有退出函数的功能，所以不必再使用分支判断
def cal_grade(grade):
    """
        根据成绩计算等级的函数

    :param grade: 浮点型成绩
    :return: None
    """
    if 0 <= grade <= 100:
        return "成绩无"
    if grade >= 90:
        return "优秀"
    if grade >= 80:
        return "良好"
    if grade >= 60:
        return "及格"
    return "不及格"


print(cal_grade(80.5))
