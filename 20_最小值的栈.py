"""
实现一个可以返回最小值的栈，要求时间复杂度为n(1)
"""


class Solution:
    """
    思路，借助一个辅助栈，压栈时只压当前的最小值
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.min_stack) == 0:
            self.min_stack.append(node)
        elif self.min() > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())

    def pop(self):
        # write code here
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.min_stack:
            return self.min_stack[-1]
