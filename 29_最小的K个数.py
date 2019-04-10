"""
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

"""
分析：
    这题的核心考点是时间复杂度：
    一般的想法是把list排序后，输出前K小的元素，即使使用快排，时间复杂度也是在O(nlogn)
    最佳算法是将list建堆，然后从堆中输出这k个元素，时间复杂度为O(logn)
"""

# 排序做法
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        a_list = sorted(tinput)
        return a_list[:k]