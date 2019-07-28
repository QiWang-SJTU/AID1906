class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0):
        """
            创建学生对象
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        # 因为id不是创建学生对象时赋予的，而是添加时赋予的，所以在这里赋值为None
        self.id = None
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
        学生管理控制器，负责处理对学生列表的逻辑操作
    """
    # 定义类变量，初始化id为1000，每次调用add_student方法时加1
    __init_id = 1000

    def __init__(self):
        # 因为学生列表不是一次性传入的，而是通过输入信息添加的，所以先赋为空
        self.__stu_list = []

    # 只读数据
    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加学生
        :param stu: 需要添加的学生对象，传入学生对象
        :return: None
        """
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)

    def __generate_id(self):
        """
            id生成器
        :return: id
        """
        # 访问类变量   类名.类变量  id增加1
        StudentManagerController.__init_id += 1
        # 返回id
        return StudentManagerController.__init_id

    def remove_student(self, stu_id):
        """
            移除学生信息
        :param stu_id: 需要移除的学生编号
        :return: 是否移除成功，True:成功 False:失败
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list) - 1):
            for j in range(i, len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]


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


view = StudentManagerView()
view.main()
