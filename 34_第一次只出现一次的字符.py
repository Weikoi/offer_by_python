"""
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
"""
from collections import OrderedDict


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1

        stat_dict = OrderedDict()
        for i in s:
            stat_dict[i] = stat_dict.get(i, 0) + 1

        for i in stat_dict:
            if stat_dict[i] == 1:
                return s.index(i)
