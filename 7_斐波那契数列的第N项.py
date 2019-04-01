# 题目：现在要求输入一个整数n，请你输出斐波那契数列的第n项。


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        print("here")
        i = 1
        a = 1
        b = 1
        while (i < n):
            a, b = b, a + b
            print(a, b)
            i += 1
        return a


if __name__ == '__main__':
    print(fib(5))


# answer
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]
