import sys

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    line1_list = line1.split()
    n = int(line1_list[0])
    w = int(line1_list[1])
    print('n=',n,'w=',w)
    line2 = sys.stdin.readline().strip()
    line2_list = sorted([int(i) for i in line2.split()])
    print(line2_list)
    l = min(line2_list[0], line2_list[len(line2_list) // 2] / 2)

    print(min(3 * n * l, w))