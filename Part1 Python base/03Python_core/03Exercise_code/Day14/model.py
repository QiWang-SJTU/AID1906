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
