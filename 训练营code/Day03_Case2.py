s = input("请输入字符串：")
for i in range(0,int(len(s)/2)-1):
    if s[i] != s[len(s)-i-1]:
        print("不是回文")
    else:
        break
print("是回文")



