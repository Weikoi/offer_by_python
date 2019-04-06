""""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 原地合并
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head_node = ListNode(0)
        cur = head_node

        pointer1 = pHead1
        pointer2 = pHead2

        while pointer1 is not None and pointer2 is not None:
            if pointer1.val <= pointer2.val:
                cur.next = pointer1
                pointer1 = pointer1.next
            else:
                cur.next = pointer2
                pointer2 = pointer2.next
            cur = cur.next

        if pointer1 is None:
            cur.next = pointer2
        else:
            cur.next = pointer1
        return head_node.next


# 开新内存收集所有元素后排序，再建立新链表
class Solution2:

    def Merge(self, pHead1, pHead2):
        # write code here
        res = []
        while pHead1:
            res.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            res.append(pHead2.val)
            pHead2 = pHead2.next
        res.sort()
        dummy = ListNode(0)
        pre = dummy
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return dummy.next
