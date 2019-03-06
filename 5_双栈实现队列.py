'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
这一题还是挺难的，有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
23ms
5628k
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, node):
        self.stack_a.append(node)

    def pop(self):
        if len(self.stack_b) == 0:
            if len(self.stack_a) == 0:
                return None
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
        else:
            return self.stack_b.pop()


# results
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()
