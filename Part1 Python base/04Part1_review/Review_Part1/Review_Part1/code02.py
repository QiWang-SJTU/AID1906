"""
    17:15
    面向对象
        概述
            面向过程:干  关心步骤(过程)
            面向对象:找  关心谁(对象)?干嘛
            经典案例:购物车code/day09/day08_exercise/shopping
                    购物车code/day15/shopping_oo
        三大特征
            封装:分
                 具体影响效果(负责处理具体功能)
                 技能释放器(负责根据需求创建具体影响效果)
            继承:隔
                影响效果(隔离释放器与具体效果的变化)
            多态:执
                具体影响效果重写影响效果
                根据需求创建具体影响效果对象

        六大原则
            开闭:增加新效果,不影响其他代码.
            单一:每个功能都只负责一个变化点
            依赖倒置:释放器调用影响效果(父),不调用具体影响效果(子)
            组合复用:释放器存储影响效果变量
            里氏替换:...
            迪米特:谁都不影响谁

        经典案例:技能系统code/day14/day13_exercise/exercise01

        关系
            泛化(继承)
            组合(变量)
技能系统code / day14 / day13_exercise / exercise01

class 影响效果
    ...

class 消耗法力(影响效果)

    ...
class ...(影响效果)
    ...

class 技能释放器
    准备技能()
        读取配置文件,根据技能名称,获取影响效果名称
        创建具体影响效果对象eval("....")

    生成技能()
        调用影响效果,执行具体影响效果.

变量 = 技能释放器("降龙十八掌")
变量.生成技能()
"""


class Student:
    def __init__(self, name=""):
        self.name = name


s01 = Student("老大")
list01 = [
    s01,
    Student("老二"),
    Student("老三"),
]


def fun01(list_target):
    # 修改列表第一个元素
    list_target[0] = Student("大哥")
    # 修改列表第二个元素指向的对象
    list_target[1].name = "二哥"
    # 修改栈帧中的局部变量
    list_target = Student("三弟")


fun01(list01)
print(s01.name)  # "老大"
print(list01[0].name)  # 大哥
print(list01[1].name)  # 二哥
print(list01[2].name)  # 老三
