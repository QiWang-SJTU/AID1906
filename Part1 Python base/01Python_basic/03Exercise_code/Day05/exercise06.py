out_list = []
while True:
    in_str = input("请输入字符串: ")
    if not in_str:
        break
    out_list.append(in_str)
    out_str = "".join(out_list)
print(out_str)


