'''
题目：输入一个链表，从尾到头打印链表每个节点的值
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#  思路一：用空间复杂度换时间复杂度，遍历过程中用顺序表来存每个节点的值就好了
#  思路二：使用头插法，重新建立新的链表，然后重新遍历新的链表打印值。

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        node = listNode
        result_list = []
        if listNode.val is None:
            return None
        else:
            while node.next is not None:
                result_list.append(node.val)

            result_list.append(node.val)
        return result_list[::-1]



class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return None
        node = listNode
        result_list = []
        while node:
            result_list.insert(0, node.val)
            node = node.next
        return result_list





# result：
'''
方法一：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
26ms
5512k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        while listNode.next is not None:
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])

        return result[::-1]

'''
方法二： 使用insert直接在头部插入
26ms
6336k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        head = listNode

        while head:
            result.insert(0, head.val)
            head = head.next
        return result