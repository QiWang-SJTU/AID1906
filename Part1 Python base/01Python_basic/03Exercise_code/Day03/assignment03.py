age = int(input("请输入年龄： "))
if age <= 0:
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
