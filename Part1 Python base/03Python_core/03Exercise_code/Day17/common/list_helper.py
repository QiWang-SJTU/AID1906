"""
     工具类:定义针对可迭代对象的常用操作
     # todo 添加新功能(获取最小、降序、倒序查找)
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找多个元素.

        :param iterable: 需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return: 所有满足条件的对象
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找单个元素.

        :param iterable: 需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return item: 第一个满足条件的对象
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_num(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找满足条件的元素个数.

        :param iterable: 需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return num: 满足条件的对象个数
        """
        num = 0
        for item in iterable:
            if func_condition(item):
                num += 1
        return num

    @staticmethod
    def is_exist(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中判断是否具有满足条件的对象.

        :param iterable: 需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return bool: 存在时返回True, 不存在时返回False
        """
        for item in iterable:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum_item(iterable, func_condition):
        """
            在可迭代对象中根据指定条件求和.

        :param iterable: 需要求和的可迭代对象
        :param func_condition: 函数类型的求和条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return sum_result 求和结果
        """
        sum_result = 0
        for item in iterable:
            sum_result += func_condition(item)
        return sum_result

    @staticmethod
    def select_info(iterable, func_condition):
        """
            在可迭代对象中根据指定条件对每个元素进行筛选.

        :param iterable: 需要筛选的可迭代对象
        :param func_condition: 函数类型的筛选条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return 生成器对象类型的筛选结果
        """
        for item in iterable:
            yield func_condition(item)

    @staticmethod
    def get_max(iterable, func_condition):
        """
            在可迭代对象中根据指定条件获取最大值

        :param iterable: 需要筛选的可迭代对象
        :param func_condition: 函数类型的筛选条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return 最大的对象
        """
        max_item = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(max_item) < func_condition(iterable[i]):
                max_item = iterable[i]
        return max_item

    @staticmethod
    def get_min(iterable, func_condition):
        """
            在可迭代对象中根据指定条件获取最小值

        :param iterable: 需要筛选的可迭代对象
        :param func_condition: 函数类型的筛选条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return 最小的对象
        """
        min_item = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(min_item) > func_condition(iterable[i]):
                min_item = iterable[i]
        return min_item

    @staticmethod
    def order_by(iterable, func_condition):
        """
            在可迭代对象中根据指定条件升序排列

        :param iterable: 需要排序的可迭代对象
        :param func_condition: 函数类型的排序条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return
        """
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if func_condition(iterable[i]) > func_condition(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]

    @staticmethod
    def order_by_descend(iterable, func_condition):
        """
            在可迭代对象中根据指定条件降序排列

        :param iterable: 需要排序的可迭代对象
        :param func_condition: 函数类型的排序条件
              func_condition(可迭代对象中的元素) ---> 任意类型
        :return
        """
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if func_condition(iterable[i]) < func_condition(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]