"""
    继承 -- 方法
        财产:钱不用儿子挣,但是可以花.
        皇位:江山不用太子打,但是可以坐.
        编程:代码不用子类写,但是可以用.
"""
class Person:
    def say(self):
        print("说话")

class Student(Person):
    def study(self):
        print("学习")

class Teacher(Person):
    def teach(self):
        print("讲课")

# 创建父类型对象,只能访问父类型成员
p01 = Person()
p01.say()

# 创建子类型对象,能访问父类型成员,还能访自身成员
s01 = Student()
s01.say()
s01.study()

# "是不是 实例"
# s01的对象 是 一种 Student类型
print(isinstance(s01,Student))# True
print(isinstance(s01,Person))# True
print(isinstance(s01,Teacher))# False

# s01的类型 等于 Student类型
print(type(s01) == Student)# True
print(type(s01) == Person)# False

# Student 类型 是一种 Person类型
print(issubclass(Student,Person))# True
print(issubclass(Student,Student))# True
print(issubclass(Student,Teacher))# False


# 练习:定义父类(动物,行为--吃)
#     定义子类(狗,行为-- 跑)
#     定义子类(鸟,行为-- 飞)
#     分别创建父类子类对象,调用其行为.
#     体会isinstance  type  issubclass三者之间的关系




















