"""
     工具类:定义针对可迭代对象的常用操作
     微软 LINQ  语言集成查询框架
     集成操作框架
"""

class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找多个元素.
        :param iterable:需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return:所有满足的条件
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """
            根据指定条件,在可迭代对象中查找单个元素.
        :param iterable:需要检索的可迭代对象
        :param func_condition: 函数类型的查找条件
              func_condition(可迭代对象中的元素) --> bool
        :return:第一个满足条件的对象
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable, func_condition):
        """
             在可迭代对象中获取满足条件的元素数量.
         :param iterable:需要检索的可迭代对象
         :param func_condition: 函数类型的查找条件
               func_condition(可迭代对象中的元素) --> bool
         :return:满足条件的数量
         """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def is_exists(iterable, func_condition):
        """
             在可迭代对象中判断是否具有满足条件的元素.
         :param iterable:需要检索的可迭代对象
         :param func_condition: 函数类型的查找条件
               func_condition(可迭代对象中的元素) --> bool
         :return:是否存在 True表示存在,False表示不存在
         """
        for item in iterable:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(iterable, func_condition):
        """
             在可迭代对象中根据指定条件进行求和计算
         :param iterable:需要求和的可迭代对象
         :param func_condition: 函数类型的求和条件
               func_condition(可迭代对象中的元素) --> 任意类型
         :return:求和的结果
         """
        sum_value = 0
        for item in iterable:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def select(iterable, func_condition):
        """
             在可迭代对象中根据指定条件对每个元素进行筛选
         :param iterable:需要筛选的可迭代对象
         :param func_condition: 函数类型的筛选条件
               func_condition(可迭代对象中的元素) --> 任意类型
         :return:生成器对象类型的筛选结果
         """
        for item in iterable:
            yield func_condition(item)

    @staticmethod
    def get_max(iterable, func_condition):
        """
             在可迭代对象中根据指定条件获取最大元素
         :param iterable:需要搜索的可迭代对象
         :param func_condition: 函数类型的搜索条件
               func_condition(可迭代对象中的元素) --> 任意类型
         :return:最大元素
         """
        max_item = iterable[0]
        for i in range(1, len(iterable)):
            # if max_item.atk <  iterable[i].atk:
            # if max_item.duration <  iterable[i].duration:
            if func_condition(max_item) < func_condition(iterable[i]):
                max_item = iterable[i]
        return max_item

    @staticmethod
    def order_by(iterable, func_condition):
        """
             根据指定条件对可迭代对象进行升序排列
         :param iterable:需要排序的可迭代对象
         :param func_condition: 函数类型的排序依据
               func_condition(可迭代对象中的元素) --> 任意类型
         """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].atk > iterable[c].atk:
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    # 获取最小
    # 降序
    # 删除
