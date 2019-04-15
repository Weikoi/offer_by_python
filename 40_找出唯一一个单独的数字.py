class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None
        result = array[0]
        for i in array[1:]:
            result = result ^ i
        return result
