# 练习3:定义列表升序排列函数[13,5,15,6,7]
# 核心思想:列表中所有元素俩俩比较，发现更小的则交换两个元素.
# 用第一个元素与后面的元素进行比较,
# 用第二个元素与后面的元素进行比较,
# 用第三个元素与后面的元素进行比较,
# ....
# 用倒数第二个元素与后面的元素进行比较,

def sort(list_target):
    # 获取需要与后面比较的数据（除去最后一个）list_target[r]
    for r in range(len(list_target)-1):
        # 与后面 list_target[c] 元素进行比较
        for c in range(r+1,len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r],list_target[c] = list_target[c],list_target[r]

list01 = [13,5,15,6,7]
sort(list01)
print(list01)







