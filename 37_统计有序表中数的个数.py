class Solution:
    # 二分法找到k值的位置
    def BinarySearch(self, data, mlen, k):
        start = 0
        end = mlen - 1
        while start <= end:
            mid = (start + end) / 2
            if data[mid] < k:
                start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                return mid
        return -1

    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        index = self.BinarySearch(data, len(data), k)
        count = 0
        for i in range(index, len(data)):
            if data[i] == k:
                count += 1
        for i in range(index):
            if data[i] == k:
                count += 1
        return count

