"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return

        root = sequence.pop()

        limit = 0
        for idx, node in enumerate(sequence[:-1]):
            if node > root:
                break
            limit += 1

        for i in sequence[limit:-1]:
            if i < root:
                return False

        left = True
        if limit > 0:
            left = self.VerifySquenceOfBST(sequence[:limit])

        right = True
        if limit < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[limit:-1])

        return left and right
