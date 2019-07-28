# 列表解析式嵌套，全排列

list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶"]

list_result = []
for i in list01:
    for j in list02:
        list_result.append(i + j)
print(list_result)

list_result_1 = [i + j for i in list01 for j in list02]
print(list_result_1)











