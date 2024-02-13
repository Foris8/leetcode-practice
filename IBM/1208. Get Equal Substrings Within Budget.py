class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        i = j = cost = 0
        while j < len(s):
            cost += abs(ord(s[j]) - ord(t[j]))
            while cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
