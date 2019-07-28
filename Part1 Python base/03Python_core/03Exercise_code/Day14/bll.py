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
