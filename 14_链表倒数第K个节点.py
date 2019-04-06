'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k < 1:
            return None
        else:
            first = head
            second = head
            k = k - 1
            while k > 0:
                if first.next is not None:
                    first = first.next
                    k -= 1
                else:
                    return None
            while first.next is not None:
                first = first.next
                second = second.next
            return second
