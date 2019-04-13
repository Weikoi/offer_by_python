"""

题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

"""
大致思路：
  （1）我们可以先思考只有两个数字的情况： [3,32] ，可以看出来 332>323 因此需要把数组改变为 [32,3] ；
  （2）对于有三个数字的情况： [3,32,321] 我们两两进行比较， 332>323 于是，将 3 与 32 交换位置变成 [32,3,321] 而 3321>3213 于是将 3 与 321 继续交换位置到 [32,321,3] ；接着我们继续使用 32 进行比较，由于 32321>32132 将 32与321 进行位置交换为 [321,32,3] 此时，将数组链接起来变成 321323 即为最小的数。
  具体思路：
  （1）先将数字列表转化成字符串链表，这样便于在一个字符串后面直接加上另外一个字符串。也就是 "3"+"321"="3321" 。
  （2）构造一个比较函数，当 str1+str2>str2+str1 时我们认为字符串 str1>str2 。
  （3）将字符串列表按照比较函数的规定进行冒泡排序（或其它方法排序），将定义为”大”的字符串放到最后。而”小”的字符串放在前面。最后将字符串列表链接起来，便是所求。
"""


class Solution:
    def theMax(self, str1, str2):
        '''定义字符串比较函数'''
        return str1 if str1 + str2 > str2 + str1 else str2

    def PrintMinNumber(self, numbers):
        """使用冒泡进行排序(把最大的放最后)"""
        string = [str(num) for num in numbers]
        res = []
        flag = True
        count = len(string) - 1
        while flag and count > 0:
            flag = False
            for i in range(len(string) - 1):
                if self.theMax(string[i], string[i + 1]) == string[i]:
                    temp = string[i]
                    del string[i]
                    string.insert(i + 1, temp)
                    flag = True
            count -= 1
        string = ''.join(string)
        return string


if __name__ == '__main__':
    result = Solution()
    print(result.PrintMinNumber([3, 32, 321]))
