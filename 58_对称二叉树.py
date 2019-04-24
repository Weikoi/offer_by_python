class Solution:
    def isSymmetrical(self, root):
        # write code here
        if not root:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)
