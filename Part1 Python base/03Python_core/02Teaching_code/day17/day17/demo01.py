"""
    lambda : 匿名函数
    语法规则:lambda 参数:函数体
"""
# 定义有参数lambda
func = lambda item:item % 2 == 0
re = func(5)
print(re)

# 定义无参数lambda
func = lambda :100
re = func()
print(re)

# 定义多个参数lambda
func =lambda a,b,c:a+b+c
re = func(1,2,3)
print(re)

# 定义无返回值lambda
func = lambda a:print("变量是:",a)
func(10)

class A:
    def __init__(self,a):
        self.a = a

def fun01(obj):
    obj.a = 100

o = A(10)
fun01(o)
print(o.a)

# SyntaxError: can't assign to lambda
# lambda 不支持赋值语句
# func = lambda obj:obj.a = 100

# lambda 只支持一条语句
def fun01(a,b):
    if a % 2 == 0:
        print(a+b)

# lambda a,b:if a % 2 == 0: print(a+b)


list01 = [4,5,5,6,767,8,10]

# def condition01(item):
#     return item % 2 == 0
#
# def condition02(item):
#     return item % 2
#
# def condition03(item):
#     return item  > 10

def find(target,func):
    for item in target:
        if func(item):
            yield item

# for item in find(list01,condition03):
#     print(item)

for item in find(list01,lambda item:item  > 10):
    print(item)










