# 题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# print("转换为二进制为：", bin(5))
# 转换为二进制为： 0b101
# 注意前面有个0b的标识符，而且bin()转出来就是str

def one_nums(n):
    bin_str = bin(n)[2:]
    count = 0
    for i in bin_str:
        if i == '1':
            count += 1
    return count


def 


if __name__ == '__main__':
    print(one_nums(5))
