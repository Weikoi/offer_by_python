"""
题目：
返回层序遍历二叉树的二维数组。

"""


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        result = []

        while queue:
            level = []
            next_level = []
            for i in queue:
                level.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            queue = next_level

            result.append(level)
        return result

