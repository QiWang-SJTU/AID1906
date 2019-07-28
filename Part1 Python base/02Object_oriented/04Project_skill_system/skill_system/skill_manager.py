class Myclass02:
    def method02(self):
        print("skill_manager--->method02")


# import my_project.skill_system.skill_deployer as ex04
#
# class03 = ex04.Myclass03()
# class03.method03()

from skill_system.skill_deployer import Myclass03

cl3 = Myclass03()
cl3.method03()
# Myclass03().method03()

# import my_project.common.list_helper as ex05
#
# ex05.Myclass04.method04()

from common.list_helper import Myclass04

Myclass04.method04()
