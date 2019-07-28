# for x in "abc":
#     print(x)
# else:
#     print("结束")

# n = ord("a")
# while n <= ord("c"):
#     print(chr(n))
#     n += 1

# for i in range(1,10,2):  #包含开始，不包含结束，步长为1可以省略不写，开始为0可以省略不写
#     print(i,end = " ")

# for i in range(100,1000):
#     a = i//100
#     b = i%100//10
#     c = i%10
#
#     if i == a**3 + b**3 + c**3:
#         print(i,end = " ")
#     else:
#         pass


# n = int(input("请输入数值："))
# m = 0
# for i in range(1,n+1,2):
#     if m%10 != 0 or m == 0:
#         print(i, end = ' ')
#         m += 1
#     else:
#         m += 1
#         print()

# for x in "abc":
#     for y in "123":
#         print(x+y)

# for 改写练习1
# for i in range(0,5):
#     for j in range(i+1,i+6):
#         print(j, end =" ")
#     print("\n")
#
# #for 改写练习2
# for i in range(0,5):
#     for j in range(5*i+1,5*i+6):
#         print(j, end =" ")
#     print("\n")

#for 改写练习3：九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#             print('%d * %d = %d' %(j,i,j*i), end = " ", sep = '')
#     print()

# n = 0
# while n < 10:
#     n += 1
#     if n ==5:
#         continue
#     print(n)

#练习1
# n = int(input("请输入："))
# if n <= 1:
#     print("不为质数")
# else:
#     for i in range(2,n):
#         if n%i == 0:
#             print("不为质数")
#             break
#     else:
#         print("为质数")

#练习2
# for j in range(2,101):
#     if j == 2:
#         print(j," ")
#     else:
#         for i in range(2,j):
#             if j%i == 0:
#                 break
#         else:
#             print(j, end=" ")

#作业1：分解质因数
# n = int(input("请输入："))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i,end=" ")
# else:
#     pass

#作业2：打印国际象棋棋盘
for i in range(1,9):
    for j in range(1,9):
        if i%2 !=0:
            if j%2 != 0:
                print("*",end=" ")
            else:
                print("0",end=" ")
        else:
            if j%2 != 0:
                print("0",end=" ")
            else:
                print("*",end=" ")
    if j == 8:
        print()
    else:
        pass

