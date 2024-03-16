class Solution:
    def minSwaps(self, s: str) -> int:
        # sliding window -> use two pointer
        # 1111110000
        # 1 0 1 1 1 1 0
        #     left
        #           right

        # next_s: "0"
        # 110001
        # 101010 -> ans = 1 + 1 + 1 + 1
        # 010101 -> 1 + 1 =
        ch = Counter(s)
        if abs(ch["1"] - ch["0"]) > 1:
            return -1

        odd, even = 0, 0
        next_s, next_s1 = "0", "1"

        for i in range(len(s)):
            if s[i] == next_s:
                odd += 1
            else:
                even += 1

            next_s, next_s1 = next_s1, next_s

        if odd % 2 != 0:
            return even // 2
        elif even % 2 != 0:
            return odd // 2
        else:
            return min(odd//2, even//2)
