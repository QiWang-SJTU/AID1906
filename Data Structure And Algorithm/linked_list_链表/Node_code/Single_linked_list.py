"""
   单向链表的代码实现
"""


class Node(object):
    """节点"""

    def __init__(self, elem):
        # elem存放数据元素
        self.elem = elem
        # next存放下一个结点的标识
        self.next = None


class SingleLinkList(object):
    """单向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

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
            pre = self.__head
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
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到了指定元素
            if cur.elem == item:
                # 如果第一个就是要删除的结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            # 第一个不是则继续按链表后移结点
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False

    def clear(self):
        """清空链表"""
        self.__head = None


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.travel()
    ll.insert(2, 100)
    ll.insert(4, 200)
    ll.travel()

    ll.remove(5)
    ll.travel()
    ll.remove(1)
    ll.travel()
