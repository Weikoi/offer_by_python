"""
给一个链表，翻转它，返回新的头结点
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversed_linkedlist(self, head):
        # 检查初始条件
        if not head:
            return None
        # 返回的头结点初始化
        reversed_node = ListNode(-1)
        reversed.next = head
        # 定义指针
        prev = head
        cur = prev.next
        # 翻转遍历
        while cur:
            prev.next = cur.next
            cur.next = reversed_node.next
            reversed_node.next = cur
            cur = prev.next
        return reversed_node.next
