# 带头节点的单链表在创建时需要创建头结点，而不是头指针。


class Node:
    """节点"""

    def __init__(self, elem, next=None):
        # elem存放数据元素
        self.elem = elem
        # next存放下一个结点的标识
        self.next = next


class SingleLinkList:
    """单向链表"""

    def __init__(self):
        """创建一个头结点"""
        self.__head = Node(None)

    @property
    def head(self):
        """只读属性"""
        return self.__head

    def is_empty(self):
        """链表是否为空"""
        return self.__head.next is None

    def length(self):
        """链表长度"""
        # cur01游标，用来移动遍历节点
        cur01 = self.__head.next
        # count记录数量
        count = 0
        while cur01 is not None:
            count += 1
            cur01 = cur01.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur01 = self.__head.next
        while cur01 is not None:
            print(cur01.elem, end=" ")
            cur01 = cur01.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head.next
        self.__head.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        cur01 = self.__head
        while cur01.next is not None:
            cur01 = cur01.next
        cur01.next = node

    def insert(self, pos, item):
        """链表指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头插
        if pos <= 0:
            self.add(item)
        # 若指定位置pos超过链表尾部，则执行尾插
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到位置插入
        else:
            node = Node(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head.next
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        # 如果存在多个相同元素，只删除第一个
        # cur01 = self.__head.next
        # pre = None
        # while cur01 is not None:
        #     # 找到了指定元素
        #     if cur01.elem == item:
        #         # 如果第一个就是要删除的结点
        #         if cur01 == self.__head.next:
        #             self.__head.next = cur01.next
        #         else:
        #             pre.next = cur01.next
        #         break
        #     # 第一个不是则继续按链表后移结点
        #     else:
        #         pre = cur01
        #         cur01 = cur01.next

        cur01 = self.__head
        while cur01.next is not None and cur01.next.elem != item:
            cur01 = cur01.next
        if cur01.next is None:
            raise ValueError("x not in single linked list")
        else:
            cur01.next = cur01.next.next

    def search(self, item):
        """查找节点是否存在"""
        cur01 = self.__head.next
        while cur01 is not None:
            if cur01.elem == item:
                return True
            cur01 = cur01.next
        return False

    def get_value(self, index):
        if type(index) != int:
            raise TypeError("index must be int")
        if index < 0 or index >= self.length():
            raise IndexError("index out of range")
        cur01 = self.__head.next
        count = 0
        while cur01 is not None:
            if count == index:
                return cur01.elem
            count += 1
            cur01 = cur01.next

    def clear(self):
        """清空链表"""
        self.__head.next = None

    def create_single_linked_list(self, list_):
        for i in range(len(list_)):
            self.append(list_[i])


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()
    print(ll.is_empty())
    print(ll.length())
    ll.insert(1, 10)
    ll.travel()
    ll.remove(1)
    ll.travel()
    ll.remove(2)
    ll.travel()
    ll.add(100)
    ll.add(200)
    ll.travel()
    print(ll.search(100))
    print(ll.get_value(0))
