# 题目：一个链表中包含环，请找出该链表的环的入口结点。

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        if not pHead:
            return None

        cur1 = cur2 = pHead
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next.next

        flag = cur1
        len_of_circle = 1
        while cur1.next != flag:
            cur1 = cur1.next
            len_of_circle += 1

        pt1 = pt2 = pHead
        while len_of_circle > 0:
            pt1 = pt1.next
            len_of_circle -= 1

        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next

        return pt1