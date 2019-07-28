from HeadNode_single_linked_list import SingleLinkList


def merge_two_sorted_linked_list(ll01, ll02):
    """
        给出两个有序的链表ll01,ll02
        在不创建新的链表的基础上将两个链表合并为一个
        要求合并后的链表仍为有序

    :param ll01: 有序单链表
    :param ll02: 有序单链表
    :return: None
    """
    cur1 = ll01.head
    cur2 = ll02.head.next
    while cur1.next is not None:
        if cur1.next.elem <= cur2.elem:
            cur1 = cur1.next
        else:
            temp = cur1.next
            cur1.next = cur2
            cur1 = cur1.next
            cur2 = temp
    cur1.next = cur2

if __name__ == "__main__":
    ll01 = SingleLinkList()
    ll02 = SingleLinkList()
    ll01.create_single_linked_list([2, 3, 5, 7])
    ll02.create_single_linked_list([1, 4, 6, 8, 10])
    ll01.travel()
    ll02.travel()

    merge_two_sorted_linked_list(ll01, ll02)
    ll01.travel()
