# 三大特征是主题思想，设计原则是细化的原则
# 封装：定义了冰箱、大象、老虎、狮子等类
# 继承：动物类隔离了冰箱冷藏的逻辑与大象、老虎、狮子装入的逻辑
# 多态：冰箱冷藏依赖动物类，实际执行大象、老虎、狮子
# 开闭：增加了多个动物（老虎、狮子），不改变冰箱的代码
# 单一：每个类做一件事。冰箱（冷藏）、动物类（隔离变化）。体现封装的思想
# 依赖倒置：冰箱依赖动物类，而不依赖大象、老虎、狮子
# 组合复用：冰箱的冷藏方法通过参数“目标”访问大象、老虎、狮子的“进入”方法
# 里氏替换: 大象在使用父类动物的计算耗电量功能时,选择了扩展重写
# 迪米特法则: 冰箱想调用大象的进入方法, 不是直接调用或继承,而是将大象抽象为动物类,用动物类中的方法

# 冰箱可以计算冷却物体的耗电量


class Refrigerator:
    def __init__(self):
        self.__animal_list = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animal_list.append(animal)

    def cal_total_power_consumption(self):
        total_power_consumption = 0
        for item in self.__animal_list:
            total_power_consumption += item.cal_power_consumption()
        return total_power_consumption

    # 开门
    def open(self):
        print("冰箱门打开")

    # 关门
    def close(self):
        print("冰箱门关闭")

    # 装东西
    def put_into(self, target):
        target.get_into()


class Animal:
    def __init__(self, base_power=20):
        self.base_power = base_power

    def cal_power_consumption(self):
        # pass
        return self.base_power

class Elephant(Animal):
    def __init__(self, base_power, volume):
        # self.base_power = base_power
        super().__init__(base_power)
        self.volume = volume

    def cal_power_consumption(self):
        # return self.base_power + 10 * self.volume
        return super().cal_power_consumption() + 10 * self.volume


class Tiger(Animal):
    def get_into(self):
        print("老虎进去")


class Lion(Animal):
    def get_into(self):
        print("狮子进入")

