"""
    练习:
        定义员工管理器,记录所有员工,计算总工资.
        程序员:底薪 + 项目分红
        测试员:底薪 + bug * 5
        要求:增加新的岗位,不影响员工管理器.
        指出:三大特征,四个原则.

        封装:员工管理器,程序员,测试员
        继承:员工隔离员工管理器与具体员工的变化
        多态:员工管理器调用员工,执行程序员,测试员.
        开闭:增加新的岗位,不影响员工管理器.
        单一:员工管理器(管理员工),员工(隔离变化),程序员(计算薪资),测试员(计算薪资)
        依赖倒置:员工管理器调用员工,而不调用程序员/测试员
        组合复用:员工管理器存储具体员工的变量
"""


class EmployeeManager:
    """
        员工管理器
    """

    def __init__(self):
        self.__all_employee = []

    def add_employee(self, emp):
        # 判断 emp 是员工 则 添加....?
        # if type(emp) == Employee:
        # emp 属于 员工
        if isinstance(emp, Employee):
            self.__all_employee.append(emp)

    def get_total_salary(self):
        total_sarlay = 0
        for itme in self.__all_employee:
            # 调用的是员工
            # 执行的是程序员/测试员
            total_sarlay += itme.calculate_salary()
        return total_sarlay


class Employee:
    """
        员工
        抽象的 --> 统一概念 --> 隔离变化

    """

    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        """
            计算薪资
        :return: 小数类型的薪资
        """
        return self.base_salary


class Programmer(Employee):
    """
        程序员
    """

    def __init__(self, base_salary=0, bonus=0):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        return super().calculate_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary=0, bug_count=0):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() * self.bug_count * 5

    # def calculate_salary(self):
    #     return self.base_salary * self.bug_count * 5

manager = EmployeeManager()
p01 = Programmer(32000, 50000)
manager.add_employee(p01)
manager.add_employee(Tester(8000, 2))
print(manager.get_total_salary())
