import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    n_str = sys.stdin.readline()
    a_num = 0
    b_num = 0
    for i in n_str:
        if i == '0':
            a_num += 1
        elif i == '1':
            b_num += 1
    print(max(a_num, b_num) - min(a_num, b_num))
