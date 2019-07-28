"""
5. 在控制台中获取年龄，按照如下规则打印信息.
    小于 0 岁，打印 输入有误.
    小于2岁，打印婴儿。
    小于2岁 ～ 13岁，打印儿童。
    小于13岁 ～ 20岁，打印少年。
    小于20岁 ～ 65岁，打印成年人。
    小于65岁 ～ 150岁，打印老年人。
    大于150,打印妖怪.
"""

age = int(input("请输入年龄："))
if age < 0:
    print("输入有误")
elif age < 2:
    print("婴儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("少年")
elif age < 65:
    print("成年人")
elif age < 150:
    print("老年人")
else:
    print("妖怪")
