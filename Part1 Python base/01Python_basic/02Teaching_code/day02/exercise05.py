"""
    练习1: 在控制台中录入一个半径
          输出圆形的面积(公式：3.14 * 半径的平方)
             格式：圆形面积是:xxx。
"""
radius = input("请输入半径：")  # "5"
# str --> int
radius = int(radius)
result = 3.14 * radius ** 2
print("圆形面积是:" + str(result) + "。")




