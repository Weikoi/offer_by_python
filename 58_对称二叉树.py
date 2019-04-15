class Solution:
    def isSymmetrical(self, root):
        # write code here
        if root is None:
            return True
        else:
            return (self.check(root.left, root.right))

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        if self.check(left.left, right.right) and self.check(left.right, right.left):
            return True
        else:
            return False