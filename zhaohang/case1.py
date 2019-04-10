import sys
import math


def calculate(n):
    if n < 6:
        return 0
    elif n == 6:
        return 1
    else:
        demo_list = [i for i in range(n + 1)][6:]
        demo_list.reverse()
        result = 0
        for i in demo_list:
            result += math.factorial(n - i)
    return result


n = int(sys.stdin.readline().strip())
print(calculate(n))
