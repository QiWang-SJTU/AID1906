num = int(input("请输入边长： "))
for i in range(1, num + 1):
    if i % num in [0, 1]:
        print('*' * num)
    else:
        print("*" + " " * (num - 2) + "*")
