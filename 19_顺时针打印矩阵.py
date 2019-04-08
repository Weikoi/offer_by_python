"""
顺时针打印二维矩阵
"""


# -*- coding:utf-8 -*-
class Solution:
    """
    思路是打印一次，逆时针翻转一次
    """

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result.append(matrix.pop(0))
            while not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        new_matrix = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(cols):
            new_line = []
            for j in range(rows):
                new_line.append(matrix[j][cols-i-1])
            new_matrix.append(new_line)
        return new_matrix