# 练习2. 在控制台中，循环录入一个编码值，然后打印字符串.
#        如果输入空字符，则退出程序.

while True:
    str_code = input("请输入编码值:")
    if str_code == "":
        break

    code = int(str_code)
    # 数 -->  字
    char = chr(code)
    print(char)
