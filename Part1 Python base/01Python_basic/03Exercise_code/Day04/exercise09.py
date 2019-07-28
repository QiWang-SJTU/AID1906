# input_str = input("请输入字符串： ")
# for i in input_str:
#     print(ord(i))

str_result = ""
while True:
    input_num_str = input("请输入编码值： ")
    if not input_num_str:
        break
    else:
        input_num = int(input_num_str)
        str_result += chr(input_num)
print(str_result)
