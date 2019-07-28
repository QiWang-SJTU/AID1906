"""
    10:50
    面向对象三大特征:
        封装:
            语法:
                数据:用一个类将多个变量包装起来.
                    class 类名:
                        def __init__(self,参数):
                            self.数据1 = 参数
                            self.数据2 = 参数
                            self.数据3 = 参数

                        def 方法1(self):
                            操作数据的逻辑

                        def __方法2(self):
                            操作数据的逻辑

                    变量 = 类名(参数)
                    变量.数据1
                    变量.数据2
                    变量.数据3
                    变量.方法1()

                行为: 对外隐藏实现功能的细节
                      注意:对外要提供必要的功能
            设计:
                分而治之,变则疏之.
        继承:
            语法:
                class 爸爸:
                    def __init__(self,参数1):
                        self.数据1 = 参数1

                    功能1

                class 儿子(爸爸):
                      def __init__(self,参数1,参数2):
                        super().__init__(参数1)
                        self.数据2 = 参数2

                    功能2

                变量 = 儿子()
                变量.功能1()
                变量.功能2()
            设计:
                抽象具体事物,统一概念(约束子类),隔离变化
        多态:
            语法:依赖重写实现
            重写:儿子具有和爸爸相同的方法,实际执行的是儿子的方法(覆盖)
            做法:重写 + 创建子类对象 --> 调用父执行子

                class 爸爸:
                    def 功能1(self):
                        .....
                class 儿子(爸爸):
                    def 功能1(self):
                        .....

                # 创建子类对象
                变量 = 儿子()
                变量.功能1() # 执行儿子的功能

                # 不是多态(创建父类对象)
                变量 = 爸爸()
                变量.功能1() # 执行爸爸的功能

            设计:调用父类方法,执行子类方法(创建子类对象).

                # 做函数使用父类
                def 函数(爸爸):
                    爸爸.功能1()

                # 用函数使用儿子
                函数(儿子())# 传递到函数中的是子类对象

    面向对象设计原则:
        开闭原则:允许增加新功能,不能修改以前的代码.
        单一职责:一个类处理一个变化点
        依赖倒置:调用父,而不调用子.
        组合复用:通过变量(参数/实例变量)调用,而不是通过继承调用.

    案例1:
        老张开车/坐飞机...去东北

        # 违背了:开闭原则,依赖倒置
        class 人:
            def 去(飞机):
                if 是飞机:
                    ....
                elif 是车:
                    ...
        ------------架构师---------------
        class 人:
            def 去(交通工具):
                # 现象:调用父类,执行子类.
                交通工具.运输()

        class 交通工具:
            def 运输():
                ...
        ------------程序员---------------
        # 做法1:重写
        class 飞机(交通工具):
            def 运输():
                ...
        class 车:
            def 运输():
                ...
         ------------测试---------------
        变量1 = 人()
        # 做法2:创建的是子类对象
        变量2 = 飞机()
        变量1.去(变量2)

    案例2:
        手雷爆炸伤害玩家/敌人.
        封装:手雷/玩家/敌人
        继承:受害者隔离了手雷爆炸的逻辑与玩家或者敌人受伤的逻辑
        多态:手雷爆炸依赖受害者,实际执行玩家与敌人.
        开闭:增加/减少新受害者,手雷不用改变.
        单一:手雷(爆炸) 受害者(隔离变化) 玩家(受伤逻辑) 敌人(受伤逻辑)
        依赖倒置:手雷依赖受害者,不依赖玩家/敌人.
        组合复用:手雷的爆炸方法,通过参数"受害者"访问玩家/敌人"受伤"方法

         ------------架构师---------------
        class 手雷:
            def 爆炸(受害者):
                受害者.受伤()

        class 受害者:
            def 受伤():
                ...
        ------------程序员---------------
        class 玩家(受害者):
            def 受伤():
                ...
        class 敌人(受害者):
            def 受伤():
                ...
         ------------测试---------------
        变量1 = 手雷()
        变量2 = 玩家()
        变量1.爆炸(变量2)
    案例3:
        图形管理器管理圆形/矩形.
        封装:图形管理器/圆形/矩形
        继承:图形隔离了图形管理器计算总面积的逻辑与圆形/矩形获取面积的逻辑
        多态:图形管理器依图形,实际执行圆形,矩形.
        开闭:增加/减少新图形,图形管理器不用改变.
        单一:图形管理器(管理图形) 图形(隔离变化) 圆形(获取面积) 矩形(获取面积)
        依赖倒置:图形管理器依赖图形,不依赖圆形/矩形.
        组合复用:图形管理器的计算总面积方法,通过实例变量"所有图形"访问圆形/矩形"获取面积"方法

         ------------架构师---------------
        class 图形管理器:
            def __init__():
                self.所有图形 = []

            def 计算总面积():
                for 图形 in self.所有图形:
                    累加 图形.获取面积()

        class 图形:
            def 获取面积():
                ...
        ------------程序员---------------
        class 圆形(图形):
            def 获取面积():
                ...
        class 矩形(图形):
            def 获取面积():
                ...
         ------------测试---------------
        变量1 = 图形管理器()
        变量2 = 圆形()
        变量1.添加图形(变量2)
        变量1.计算总面积()
"""