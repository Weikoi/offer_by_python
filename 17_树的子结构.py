"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.is_sub(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        return result

    def is_sub(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        elif not pRoot1:
            return False
        elif pRoot1.val == pRoot2.val:
            return self.is_sub(pRoot1.right, pRoot2.right) and self.is_sub(pRoot1.left, pRoot2.left)
        else:
            return False
