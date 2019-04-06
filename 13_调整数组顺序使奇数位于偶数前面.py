'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:
    def reOrderArray(self, array):
        list_odd = []
        list_even = []
        for i in array:
            if i % 2 == 0:
                list_even.append(i)
            else:
                list_odd.append(i)
        return list_odd + list_even
