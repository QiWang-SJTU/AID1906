# 封装: 员工管理器, 程序员, 测试员
# 继承: 员工隔离员工管理器与具体员工的变化
# 多态: 员工管理器调用员工, 执行程序员, 测试员.
# 开闭: 增加新的岗位, 不影响员工管理器.
# 单一: 员工管理器(管理员工), 员工(隔离变化), 程序员(计算薪资), 测试员(计算薪资)
# 依赖倒置: 员工管理器调用员工, 而不调用程序员 / 测试员
# 组合复用: 员工管理器存储具体员工的变量


class StaffManager:
    def __init__(self):
        self.__staff_list = []

    def add_staff(self, staff):
        # 判断staff属于员工类则添加
        if isinstance(staff, Staff):
            self.__staff_list.append(staff)

    def cal_total_salary(self):
        total_salary = 0
        for item in self.__staff_list:
            total_salary += item.cal_salary()
        return total_salary


class Staff:
    # def __init__(self, based_salary=20):
    #     self.based_salary = based_salary

    def cal_salary(self):
        pass
        # return self.based_salary


class Programmer(Staff):
    def __init__(self, based_salary, project_bonus):
        # super().__init__(based_salary)
        self.based_salary = based_salary
        self.project_bonus = project_bonus

    def cal_salary(self):
        # 里氏替换，扩展重写
        # return super().cal_salary() + self.project_bonus
        return self.based_salary + self.project_bonus


class Tester(Staff):
    def __init__(self, based_salary, bug):
        # super().__init__(based_salary)
        self.based_salary = based_salary
        self.bug = bug

    def cal_salary(self):
        # 里氏替换，扩展重写
        # return super().cal_salary() + self.bug * 5
        return self.based_salary + self.bug * 5


m1 = StaffManager()
p01 = Programmer(20, 1)
t01 = Tester(20, 10)
m1.add_staff(p01)
m1.add_staff(t01)
print(m1.cal_total_salary())
