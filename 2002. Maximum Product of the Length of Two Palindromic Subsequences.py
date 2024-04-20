class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali = len(s), {}  # bitmask:length

        for mask in range(1, 1 << n):  # 1<<n 是把1往左边移动n位
            subseq = ""

            for i in range(n):
                if mask & (1 << i):  # 检查哪个位置有 “1”
                    subseq += s[i]

            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        res = 0

        for mask1, length1 in pali.items():
            for mask2, length2 in pali.items():
                if mask1 & mask2 == 0:  # no overlapping
                    res = max(res, length1 * length2)
        return res
