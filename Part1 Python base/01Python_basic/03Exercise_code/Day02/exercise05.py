v_init = float(input("请输入初速度："))
t_time = float(input("请输入时间："))
s_distance = float(input("请输入距离："))

a = 2*(s_distance-v_init*t_time)/(t_time**2)
print("加速度是：" + str(a))
