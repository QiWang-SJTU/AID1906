# 练习:在控制台中循环录入字符串，如果录入空字符，则停止录入。
#      打印所有录入的内容。

list_result = []
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    list_result.append(str_input)

str_result = "".join(list_result)
print(str_result)

