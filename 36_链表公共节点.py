# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        while not pHead1 or not pHead2:
            return None
        cur1 = pHead1
        cur2 = pHead2

        length1 = 0
        length2 = 0
        while cur1.next:
            length1 += 1
            cur1 = cur1.next

        while cur2.next:
            length2 += 1
            cur2 = cur2.next

        if length1 > length2:
            count = 0
            while count < length1 - length2:
                pHead1 = pHead1.next
                count += 1

        else:
            count = 0
            while count < length1 - length2:
                pHead2 = pHead2.next
                count += 1

        while (pHead1 != pHead2):
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1