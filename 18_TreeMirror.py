"""
翻转二叉树
"""


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        else:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.Mirror(root.right)
            self.Mirror(root.left)
            return root
