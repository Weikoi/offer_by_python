class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 核心思路是判断二叉树的深度


class Solution:
    def getDeepth(self, Root):
        if Root is None:
            return 0
        nright = self.getDeepth(Root.right)
        nleft = self.getDeepth(Root.left)
        return max(nright, nleft) + 1

    def IsBalance_solution(self, pRoot):
        if pRoot is None:
            return True
        right_dep = self.getDeepth(pRoot.right)
        left_dep = self.getDeepth(pRoot.left)
        return self.IsBalance_solution(pRoot.right) and self.IsBalance_solution(pRoot.left) and abs(
            right_dep - left_dep) < 2
