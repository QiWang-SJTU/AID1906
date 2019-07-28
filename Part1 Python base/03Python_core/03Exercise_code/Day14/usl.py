from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
        学生管理器视图,负责处理界面逻辑.
    """

    def __init__(self):
        # 将StudentManagerController类的对象作为一个私有变量
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)成绩排序")

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__order_student()

    def main(self):
        """
            主函数，先显示再选择
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        while True:
            # 创建学生对象
            stu = StudentModel()
            # 添加信息
            stu.name = input("请输入姓名：")
            if stu.name == "":
                break
            stu.age = int(input("请输入年龄："))
            stu.score = int(input("请输入分数："))

            # 得到学生信息后要调用add方法，但add是在StudentManagerController类里面的
            # 必须通过StudentManagerController类的对象来访问。
            # 所以常规的想法是先创建一个类，再调用方法，如下：

            # controller = StudentManagerController()
            # controller.add_student(stu)

            # 但是这样每次都要创建一个新的类，每次调用时都创建一个新列表存放学生对象
            # 这样无法将学生都添加到一个列表中，不符合要求

            # 所以我们采用下面的做法：把类对象作为私有变量，只有一个对象，存放在一个列表中
            self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        # 根据学生id删除,界面只做输入输出操作，不处理逻辑
        student_id = int(input("请输入需要删除的学生id："))
        if self.__controller.remove_student(student_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        # 根据学生id修改
        stu = StudentModel()
        stu.id = int(input("请输入要修改的学生id："))
        stu.name = input("请输入修改后的姓名：")
        stu.age = int(input("请输入修改后的年龄："))
        stu.score = int(input("请输入修改后的分数："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __order_student(self):
        self.__controller.order_by_score()
