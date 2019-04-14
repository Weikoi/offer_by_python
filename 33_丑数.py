'''
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n - 1):
            # print(idx2, idx3, idx5)
            res.append(min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5))
            if res[-1] == res[idx2] * 2:
                idx2 += 1
            if res[-1] == res[idx3] * 3:
                idx3 += 1
            if res[-1] == res[idx5] * 5:
                idx5 += 1
            print(res)
        return res[-1]

    def GetUglyNumber_Solution2(self, index):
        # write code here
        result = [1]

        idx2 = 0
        idx3 = 0
        idx5 = 0

        cur = 1
        while cur < index:
            result.append(min(result[idx2] * 2, result[idx3] * 3, result[idx5] * 5))
            # print(idx2, idx3, idx5)
            if result[-1] == result[idx2] * 2:
                idx2 += 1
            if result[-1] == result[idx3] * 3:
                idx3 += 1
            if result[-1] == result[idx5] * 5:
                idx5 += 1

            cur += 1
            print(result)
        return result[-1]


if __name__ == '__main__':
    result = Solution()
    print(result.nthUglyNumber(10))
    print(result.GetUglyNumber_Solution2(10))
