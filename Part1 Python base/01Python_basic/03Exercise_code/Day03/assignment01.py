num_start = int(input("请输入开始值： "))
num_stop = int(input("请输入结束值： "))

# while num_start < num_stop - 1:
#     num_start += 1
#     print(num_start)
# while num_start > num_stop + 1:
#     num_start -= 1
#     print(num_start)

direction = 1 if num_stop > num_start else -1

while num_start != num_stop - direction:
    num_start += direction
    print(num_start)
