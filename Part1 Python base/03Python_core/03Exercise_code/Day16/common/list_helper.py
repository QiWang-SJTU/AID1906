"""
     工具类:定义针对可迭代对象的常用操作
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找多个元素.
        :param iterable:
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return:所有满足的条件
        """
        for item in iterable:
            if func_condition(item):
                yield item
