"""
层序遍历二叉树
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here

        if not root:
            return None
        result = []
        node_queue = [root]
        while len(node_queue) != 0:
            node = node_queue.pop(0)
            result.append(node.val)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
        return result
