"""
    函数参数
        形参
            默认形参：实参可以不传递数据。
            位置形参：实参根据位置进行对应
                星号元组形参：实参数量无限（将实参合并为元组）
            关键字形参：实参根据名称进行对应
                双星号字典形参:实参数量无限（将实参合并为字典）
                命名关键字形参：实参必须是关键字实参
"""


# 1. 默认形参：实参可以不传递数据（从右向左依次存在）
def fun01(a=0, b="bb", c=1.5):
    print(a)
    print(b)
    print(c)


#
fun01()
fun01(1, "b")
# 关键实参 + 默认形参：调用者可以随意指定参数进行传递
fun01(b="bbbbb")


# 2. 星号元组形参：让位置实参的数量无限
def fun02(p1, p2, *args):
    print(args)


fun02(1, 2)
fun02(1, 2, 3)
fun02(1, 2, 3, 4, 5)


# 3. 命名关键字形参：传递的实参必须是关键字实参。
# 写法1：星号元组形参以后的参数是命名关键字形参
#   p1  p2
def fun03(*args, p1="", p2):
    print(args)
    print(p1)
    print(p2)


fun03(2, 2, p1=111, p2=222)
fun03(p1=111, p2=222)
fun03(p2=222)
# 案例：
# def print(*args, sep=' ', end='\n', file=None):
# 1---fff---3.5---4---55---6---67 ok
print(1, "fff", 3.5, 4, 55, 6, 67, sep="---", end=" ")
print("ok")


# 写法2:星号以后的位置形参是命名关键字形参
def fun04(*, p1=0, p2):
    print(p1, p2)


fun04(p1=1, p2=2)
fun04(p2=2)


# 4. 双星号字典形参:让关键字实参的数量无限
def fun05(**kwargs):
    print(kwargs)


fun05(a=1)  # {'a': 1}
fun05(a=1, b=2)
fun05(a=1, b=2, qtx=3)  # {'a': 1, 'b': 2, 'qtx': 3}


# 形参位置
# 练习1:
def fun06(a, *args, c, d="dd", **kwargs):
    print(a)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun06(1, c=3)


# 练习2:
def fun07(*args, **kwargs):
    print(args)
    print(kwargs)


fun07()
fun07(5, 6, a=154)

# 练习3:自学字符串常用函数
# (1)看看字符串都提供了哪些功能(中文含义)
# (2)参照文档自学常用函数
#   to_student_for_month01\documentation\str_method.docx
# (3)解决具体问题：
str01 = "  校训：  自 强不息,厚德 载 物.      "
# -- 查找空格的数量
# -- 删除字符串前后空格(中间的空格留着)
# -- 删除所有空格
# -- 查找"厚德"的位置
# -- 判断字符串是否一"校训"开头
