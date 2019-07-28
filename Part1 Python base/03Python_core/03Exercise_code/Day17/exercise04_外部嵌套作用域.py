# # 外部
# def fun01():
#     # 对于外部函数fun01而言，a是局部变量
#     # 对于内部函数fun02而言，a是外部嵌套变量
#     a = 10
#
#     # 内部
#     def fun02():
#         nonlocal a
#         a = 100
#
#     fun02()
#     print(a)
#
#
# fun01()


