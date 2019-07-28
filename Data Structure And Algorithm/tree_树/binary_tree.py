class Node:
    """结点类"""

    def __init__(self, elem=-1, left_child=None, right_child=None):
        self.elem = elem
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree: 
    """完全二叉树类"""

    def __init__(self, root=None):
        """根结点"""
        self.root = root

    def add(self, elem):
        """为树添加结点"""

        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            # 对已有的结点进行层次遍历(广度优先)
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left_child is None:
                    cur.left_child = node
                    return
                elif cur.right_child is None:
                    cur.right_child = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.left_child)
                    queue.append(cur.right_child)

    def breadth_travel(self):
        """利用队列实现树的广度优先遍历"""

        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end=" ")
            if cur.left_child is not None:
                queue.append(cur.left_child)
            if cur.right_child is not None:
                queue.append(cur.right_child)

    # 深度优先遍历的三种方式
    def pre_order(self, root_node):
        """递归实现先序遍历 ---> 根->左->右"""

        if root_node is None:
            return
        print(root_node.elem, end=" ")
        self.pre_order(root_node.left_child)
        self.pre_order(root_node.right_child)

    def in_order(self, root_node):
        """递归实现中序遍历 ---> 左->根->右"""

        if root_node is None:
            return
        self.in_order(root_node.left_child)
        print(root_node.elem, end=" ")
        self.in_order(root_node.right_child)

    def post_order(self, root_node):
        """递归实现后序遍历 ---> 左->右->根"""

        if root_node is None:
            return
        self.post_order(root_node.left_child)
        self.post_order(root_node.right_child)
        print(root_node.elem, end=" ")


if __name__ == "__main__":
    tree01 = BinaryTree()
    tree01.add(1)
    tree01.add(2)
    tree01.add(3)
    tree01.add(4)
    tree01.add(5)
    tree01.add(6)
    tree01.add(7)
    tree01.add(8)
    tree01.add(9)
    tree01.add(10)
    tree01.add(11)
    tree01.add(12)
    tree01.add(13)
    tree01.add(14)
    tree01.add(15)
    tree01.breadth_travel()
    print()
    tree01.pre_order(tree01.root)
    print()
    tree01.in_order(tree01.root)
    print()
    tree01.post_order(tree01.root)
