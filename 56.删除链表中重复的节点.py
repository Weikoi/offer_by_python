# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        prehead = ListNode(-1)
        prehead.next = pHead

        pre = prehead
        p = pHead
        nextnode = ListNode(0)
        while p and pre:
            nextnode = p.next

            if p.val == nextnode.val:
                while nextnode and nextnode.val == p.val:
                    nextnode = nextnode.next
                pre.next = nextnode
                p = nextnode
            else:
                pre = p
                p = p.next
        return prehead.next
