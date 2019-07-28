# 练习:在控制台中循环录入人的信息(姓名,年龄,性别,体重),如果名称为空字符串,停止录入.
#      -- 将所有人的信息打印出来(一人一行)
#      -- 打印第一个人的信息
#      -- 打印最后一个人的信息
# 数据结构：列表内嵌字典
# [
#   {"name":“无忌”,"age":28,"sex":"男","weight":80},
#   {"name":“赵敏”,"age":26,"sex":"女","weight":50},
# ]
"""
    17:15
    总结：存储多个数据，使用什么数据结构？
          根据具体需求，结合优缺点，综合考虑(两害相权其轻)
    字典：
        优：根据key获取value，速度最快.
           如果信息较多，通过键(指定的名称)获取,代码可读性偏好。

        缺:不能通过索引/切片获取元素，不灵活.
            内存占用较大

    列表
        优：能通过索引/切片获取元素，灵活.

        缺: 数据过多时，查找元素较慢.
            通过索引(整数)获取，如果信息较多，代码可读性偏差。
"""

list_person_info = []

while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    weight = float(input("请输入体重："))

    dict_info = {"name":name,"age":age,"sex":sex,"weight":weight}
    list_person_info.append(dict_info)

for dict_item in list_person_info:
    print("%s的年龄是%d,性别是%s,体重是%f"%(dict_item["name"],dict_item["age"],dict_item["sex"],dict_item["weight"]))

# 第一个人
dict_item = list_person_info[0]
print("%s的年龄是%d,性别是%s,体重是%f" % (dict_item["name"], dict_item["age"], dict_item["sex"], dict_item["weight"]))

# 最后一个人
dict_item = list_person_info[-1]
print("%s的年龄是%d,性别是%s,体重是%f" % (dict_item["name"], dict_item["age"], dict_item["sex"], dict_item["weight"]))




