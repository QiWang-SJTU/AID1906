"""
    复习
        架构
            模型Model:负责封装数据
            控制Controller:负责逻辑处理
            视图View:负责界面逻辑
        (1)需求:比如添加学生
        (2)识别对象:找谁干活
        (3)建立交互:互相调用
                  "我在哪,他在哪?"
"""


class XXController:
    def __init__(self):
        self.stu_list = []

    def add_student(self):
        print("添加学生喽")

class XXView:
    def __init__(self):
        self.controller = XXController()

    def input_students(self):
        print("获取各种信息")
        # 实例成员,使用对象操作.
        self.controller.add_student()

    def output_students(self):
        print("显示学生信息")
        for item in self.controller.stu_list:
            pass

view = XXView()
view.input_students()
view.output_students()











