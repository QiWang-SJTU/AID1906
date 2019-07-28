class Refrigerator:
    # 开门
    def open(self):
        print("冰箱门打开")
    # 关门
    def close(self):
        print("冰箱门关闭")
    # 装东西--->隔离变化
    def put_into(self, target):
        target.get_into()


class Animal:
    # 进入
    def get_into(self):
        pass

class Elephant(Animal):
    def get_into(self):
        print("大象走进去")

class Tiger(Animal):
    def get_into(self):
        print("老虎跑进去")

class Tortoise(Animal):
    def get_into(self):
        print("乌龟爬进去")


rf = Refrigerator()
el = Elephant()
rf.open()  # 冰箱门打开
rf.put_into(el)  # 大象走进去
rf.close()  # 冰箱门关闭

