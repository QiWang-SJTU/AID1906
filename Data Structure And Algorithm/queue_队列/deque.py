class Deque:
    """顺序表实现双端队列基本操作"""

    # TODO 链式双端队列
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列大小"""
        return len(self.__list)

    def add_front(self, item):
        """从头部入队"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从尾部入队"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除"""
        return self.__list.pop()


if __name__ == "__main__":
    deque = Deque()
    print(deque.is_empty())
    deque.add_front(1)
    print(deque.is_empty())
    deque.add_front(2)
    deque.add_front(3)
    deque.add_rear(4)
    deque.add_rear(5)
    deque.add_rear(6)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.remove_rear())
