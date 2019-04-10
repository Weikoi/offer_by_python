class Solution():
    def Permutation(self, ss):

        if not ss:
            return []

        char_list = list(ss)
        char_list.sort()
        pstr = []
        for idx, s in enumerate(ss):
            if idx > 0 and s == ss[idx - 1]:
                continue

            temp = self.Permutation(''.join(ss[:idx]+''.join(ss[idx:])))
            for j in temp:
                pstr.append(char_list[idx]+j)

        return pstr

