class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0

        for i in range(len(s)):
            if s[i] == "(" and count == 0:
                count += 1
            elif s[i] == "(" and count >= 1:
                res += s[i]
                count += 1
            elif s[i] == ")" and count > 1:
                res += s[i]
                count -= 1
            elif s[i] == ")" and count == 1:
                count -= 1

        return res
