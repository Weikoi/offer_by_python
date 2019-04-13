'''
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
import math

x = 100
a_list = [p for p in range(2, x) if ([p % d for d in range(2, int(p ** 0.5) + 1)])]

print(a_list)
