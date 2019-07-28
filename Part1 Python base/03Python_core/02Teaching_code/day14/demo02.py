"""
    包

python 程序结构

项目(文件夹)
    包
        模块
            类
                函数/方法
                    语句

    17:00
"""
# 需求:导入module03.py

# 方式1
import package01.package02.module03 as m3
m3.fun01()

# 方式2
# from package01.package02.module03 import fun01
# fun01()

"""
练习1：根据如下结构,创建包与模块.
my_project / 
    main.py        
    common/
        __init__.py
        double_list_helper.py
        list_helper.py
    skill_system/
        __init__.py
        skill_deployer.py
        skill_manager.py
        
练习2: 在main.py中调用double_list_helper模块中的类方法
练习3: 在main.py中调用skill_manager模块中的实例方法.
练习4: 在skill_manager中调用skill_deployer模块中的实例方法.
练习5: 在skill_manager中调用list_helper模块中的类方法.
要求:使用方式1与方式2调用
"""















