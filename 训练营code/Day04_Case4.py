m = float(input("请输入开始值："))
n = float(input("请输入结束值："))
i = int(m)+1
j = int(n)

if i < j:
    k = i
    while i <= k <= j:
        print(k, end=" ")
        k += 1

elif i > j:
    k = j
    while j <= k <= i:
        print(k, end=" ")
        k += 1
else:
    print("输入错误")



